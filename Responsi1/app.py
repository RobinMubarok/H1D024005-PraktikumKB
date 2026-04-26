import os
from flask import Flask, render_template, request
import numpy as np
import skfuzzy as fuzz
from ParaDokter import ParaDokter

app = Flask(__name__)
dokter = ParaDokter()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compute', methods=['POST'])
def compute():
    try:
        # Form Input
        inputs = {
            'tensi_sys': float(request.form['tensi_sys']),
            'tensi_dia': float(request.form['tensi_dia']),
            'bmi': float(request.form['bmi']),
            'rr': float(request.form['rr']),
            'spo2': float(request.form['spo2']),
            'hr': float(request.form['hr']),
            'pr_int': float(request.form['pr_int']),
            'qrs_dur': float(request.form['qrs_dur']),
            'ctr': float(request.form['ctr']),
            'ef': float(request.form['ef']),
            'fs': float(request.form['fs']),
            'lvidd': float(request.form['lvidd']),
            'mets': float(request.form['mets']),
            'max_hr': float(request.form['max_hr'])
        }
        
        # Nanya DrGia
        for key, val in inputs.items():
            dokter.DrGia.input[key] = val
            
        dokter.DrGia.compute()
        
        # Sederhanain
        state = {}
        prefix_map = {
            'hemo': 'Hemo', 'pompa': 'Pompa', 'konduksi': 'Konduksi', 
            'oksi': 'Oksi', 'kardio': 'Kardio', 'toleransi': 'Tol', 
            'meta': 'Meta', 'beban': 'Beban', 'efisien': 'Efisien', 
            'aero': 'Aero', 'perfusi': 'Perfusi', 'stres': 'Stres'
        }
        
        crisp_outputs = {}
    
        consequents = {c.label: c for c in dokter.DrGia.ctrl.consequents}
        
        for var_name, prefix in prefix_map.items():
            if var_name in dokter.DrGia.output:
                crisp = dokter.DrGia.output[var_name]
                crisp_outputs[var_name] = crisp
                var_obj = consequents.get(var_name)
                
                if var_obj:
                    max_term = None
                    max_mu = -1
                    # Pake membership
                    for term_name in var_obj.terms.keys():
                        mu = fuzz.interp_membership(var_obj.universe, var_obj[term_name].mf, crisp)
                        if mu > max_mu:
                            max_mu = mu
                            max_term = term_name
                            
                    # Diganti jadi biner
                    for term_name in var_obj.terms.keys():
                        key = f"{prefix}_{term_name.replace('_', '')}"
                        state[key] = 1 if term_name == max_term else 0
            else:
                crisp_outputs[var_name] = 0.0 
                var_obj = consequents.get(var_name)
                if var_obj:
                    for term_name in var_obj.terms.keys():
                        key = f"{prefix}_{term_name.replace('_', '')}"
                        state[key] = 0

        # Nanya DrTirta
        def get_diagnosa(tree, state):
            for node in tree:
                cond = node.get("kondisi")
                if not cond:
                    continue
                var_val = cond.split("=")
                var_name = var_val[0].strip()
                req_val = int(var_val[1].strip())
                
                if state.get(var_name, 0) == req_val:
                    if "diagnosa" in node:
                        return node["diagnosa"]
                    elif "cabang" in node:
                        res = get_diagnosa(node["cabang"], state)
                        if res: return res
            return None

        diagnosis = get_diagnosa(dokter.DrTirta, state)
        if not diagnosis:
            diagnosis = "Wess!! Mati kowe, rapopo"
            
        name_map = {
            'hemo': 'Indeks Hemodinamik Dasar',
            'pompa': 'Indeks Kinerja Pompa Jantung',
            'konduksi': 'Indeks Risiko Konduksi/Aritmia',
            'oksi': 'Indeks Oksigenasi Paru-Jantung',
            'kardio': 'Indeks Kardiomegali Struktural',
            'toleransi': 'Indeks Toleransi Latihan',
            'meta': 'Indeks Sindrom Metabolik',
            'beban': 'Indeks Beban Kerja Miokardium',
            'efisien': 'Indeks Efisiensi Struktural',
            'aero': 'Indeks Kapasitas Aerobik',
            'perfusi': 'Indeks Perfusi Jaringan',
            'stres': 'Indeks Stres Fisiologis'
        }
            
        return render_template('result.html', diagnosis=diagnosis, inputs=inputs, crisp_outputs=crisp_outputs, state=state, name_map=name_map)

    except Exception as e:
        return f"Error: {str(e)}", 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
