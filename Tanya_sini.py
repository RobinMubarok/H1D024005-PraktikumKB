import customtkinter
from customtkinter import *

# Nama Gejala: pueggel tangane aku....
Gejala = {
  'G1': 'nafas abnormal',
  'G2': 'suara serak',
  'G3': 'perubahan kulit',
  'G4': 'telinga penuh',
  'G5': 'nyeri bicara menelan',
  'G6': 'nyeri tenggorokan',
  'G7': 'nyeri leher',
  'G8': 'pendarahan hidung',
  'G9': 'telinga berdenging',
  'G10': 'air liur menetes',
  'G11': 'perubahan suara',
  'G12': 'sakit kepala',
  'G13': 'nyeri pinggir hidung',
  'G14': 'serangan vertigo',
  'G15': 'getah bening',
  'G16': 'leher bengkak',
  'G17': 'hidung tersumbat',
  'G18': 'infeksi sinus',
  'G19': 'berat badan turun',
  'G20': 'nyeri telinga',
  'G21': 'selaput lendir merah',
  'G22': 'benjolan leher',
  'G23': 'tubuh tak seimbang',
  'G24': 'bola mata bergerak',
  'G25': 'nyeri wajah',
  'G26': 'dahi sakit',
  'G27': 'batuk',
  'G28': 'tumbuh di mulut',
  'G29': 'benjolan dileher',
  'G30': 'nyeri antara mata',
  'G31': 'radang gendang telinga',
  'G32': 'tenggorokan gatal',
  'G33': 'hidung meler',
  'G34': 'tuli',
  'G35': 'mual muntah',
  'G36': 'letih lesu',
  'G37': 'demam'
}

# Nama Penyakit: mualessee rek nulis siji2
Penyakit = {
  'P1': 'Tonsilitis',
  'P2': 'Sinusitis Maksilaris',
  'P3': 'Sinusitis Frontalis',
  'P4': 'Sinusitis Edmoidalis',
  'P5': 'Sinusitis Sfenoidalis',
  'P6': 'Abses Peritonsiler',
  'P7': 'Faringitis',
  'P8': 'Kanker Laring',
  'P9': 'Deviasi Septum',
  'P10': 'Laringitis',
  'P11': 'Kanker Leher & Kepala',
  'P12': 'Otitis Media Akut',
  'P13': 'Contact Ulcers',
  'P14': 'Abses Parafaringeal',
  'P15': 'Barotitis Media',
  'P16': 'Kanker Nafasoring',
  'P17': 'Kanker Tonsil',
  'P18': 'Neuronitis Vestibularis',
  'P19': 'Meniere',
  'P20': 'Tumor Syaraf Pendengaran',
  'P21': 'Kanker Leher Metastatik',
  'P22': 'Osteosklerosis',
  'P23': 'Vertigo Postular',
}

# Diagnosa: ini udah tek singkat pake rapidminer looohhhh.....
Diagnosa = [
    {'G1': ['G36', 'P8']},
    {'G36':['G37', 'G4']},
    {
        'G37': ['G2', 'G5'],
        'G4': ['G7', 'P19']
    },
    {
        'G2': ['G3', 'P13'],
        'G5': ['G2', 'G6'],
        'G7': ['G12', 'P5']
    },
    {
        'G3': ['G5', 'P11'],
        'G2': ['P9', 'P6'],
        'G6': ['P10', 'G7'],
        'G12': ['G20', 'G13']
    },
    {
        'G5': ['G6', 'P14'],
        'G7': ['P1', 'P7'],
        'G20': ['P18', 'P12'],
        'G13': ['G21', 'P4']
    },
    {
        'G6': ['G8', 'P17'],
        'G21': ['P2', 'P3']
    },
    {'G8': ['G12', 'P16']},
    {'G12': ['G9', 'G20']},
    {
        'G9': ['G25', 'P22'],
        'G20': ['P20', 'P15']
    },
    {'G25': ['P21', 'P23']}
]

class PakarTHT:

    def __init__(self, window):

        self.window = window
        self.window.title("Sistem Pakar Diagnosa Penyakit THT")
        self.window.geometry("500x300")
        self.window.config(padx=20, pady=20)

        customtkinter.FontManager.load_font('Lexend_Bold.ttf')
        customtkinter.FontManager.load_font('Lexend_ExtraBold.ttf')

        self.tingkat = 0
        self.perasaan = 'G1'

        self.fon1 = ('Lexend Bold', 15)
        self.fon2 = ('Lexend ExtraBold', 20)

        self.judul = CTkLabel(master=window, font=self.fon2)
        self.judul.pack(pady=(0, 20))

        self.pertanyaan = CTkLabel(master=window, font=self.fon1)
        self.pertanyaan.pack(pady=20)

        self.ya = CTkButton(master=window, text="Ya", font=self.fon1, command=lambda: self.jawab(True))
        self.ya.pack(pady=10)

        self.tidak = CTkButton(master=window, text="Tidak", font=self.fon1, command=lambda: self.jawab(False))
        self.tidak.pack(pady=10)

        self.ulang = CTkButton(master=window, text="Mulai Diagnosa Baru", font=self.fon2, command=self.mengulang)

        self.tanya()

    def tanya(self):

        if self.perasaan.startswith('G'):
            nama_gejala = Gejala.get(self.perasaan, "Gejala tidak diketahui")
            self.pertanyaan.configure(text=f"Apakah pasien mengalami {nama_gejala}?")
        
        elif self.perasaan.startswith('P'):
            nama_penyakit = Penyakit.get(self.perasaan, "Penyakit tidak diketahui")
            self.pertanyaan.configure(text=f"Pasien sekarang mengidap \n{nama_penyakit.upper()}\n")
            
            self.ulang.pack(pady=20)
            self.ya.pack_forget()
            self.tidak.pack_forget()

    def jawab(self, jawaban):
        
            if jawaban == True:
                next_node = Diagnosa[self.tingkat][self.perasaan][1]
            else:
                next_node = Diagnosa[self.tingkat][self.perasaan][0]
    
            self.perasaan = next_node
            self.tingkat += 1
            
            self.tanya()

    def mengulang(self):

        self.tingkat = 0
        self.perasaan = 'G1'
        
        self.ulang.pack_forget()
        self.ya.pack(pady=10)
        self.tidak.pack(pady=10)
        
        self.tanya()

def main():

    customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme("sky.json")

    jendela = CTk()
    PakarTHT(jendela)
    

    jendela.resizable(False, False) 
    jendela.mainloop()

main()