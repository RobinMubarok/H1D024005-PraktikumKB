import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

class ParaDokter:

    def __init__(self):
        self.DrGia = ctrl.ControlSystemSimulation(self.mcu_ctrl_create())
        self.DrTirta = [
            {
                "kondisi": "Konduksi_Takiaritmia = 0",
                "cabang": [
                    {
                        "kondisi": "Oksi_HipoksiaRingan = 0",
                        "cabang": [
                            {
                                "kondisi": "Hemo_Normal = 0",
                                "cabang": [
                                    {
                                        "kondisi": "Pompa_GagalBerat = 0",
                                        "cabang": [
                                            {
                                                "kondisi": "Hemo_Syok = 0",
                                                "cabang": [
                                                    {
                                                        "kondisi": "Hemo_Krisis = 0",
                                                        "cabang": [
                                                            {
                                                                "kondisi": "Pompa_DisfungsiRingan = 0",
                                                                "cabang": [
                                                                    {
                                                                        "kondisi": "Pompa_Normal = 0",
                                                                        "diagnosa": "Blok Jantung (AV Block)"
                                                                    },
                                                                    {
                                                                        "kondisi": "Pompa_Normal = 1",
                                                                        "diagnosa": "PPOK / Asma Bronkial"
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "kondisi": "Pompa_DisfungsiRingan = 1",
                                                                "cabang": [
                                                                    {
                                                                        "kondisi": "Kardio_Normal = 0",
                                                                        "cabang": [
                                                                            {
                                                                                "kondisi": "Kardio_Ringan = 0",
                                                                                "diagnosa": "Penyakit Jantung Koroner (PJK)"
                                                                            },
                                                                            {
                                                                                "kondisi": "Kardio_Ringan = 1",
                                                                                "diagnosa": "Penyakit Katup Jantung (Valvular)"
                                                                            }
                                                                        ]
                                                                    },
                                                                    {
                                                                        "kondisi": "Kardio_Normal = 1",
                                                                        "diagnosa": "Intoleransi Latihan Berat"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "kondisi": "Hemo_Krisis = 1",
                                                        "cabang": [
                                                            {
                                                                "kondisi": "Pompa_Normal = 0",
                                                                "cabang": [
                                                                    {
                                                                        "kondisi": "Tol_KapasitasKurang = 0",
                                                                        "diagnosa": "Krisis Hipertensi (Emergency)"
                                                                    },
                                                                    {
                                                                        "kondisi": "Tol_KapasitasKurang = 1",
                                                                        "diagnosa": "Sindrom Metabolik Lengkap"
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "kondisi": "Pompa_Normal = 1",
                                                                "diagnosa": "Penyakit Jantung Hipertensi (HHD)"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "kondisi": "Hemo_Syok = 1",
                                                "diagnosa": "Frailty Syndrome (Kerapuhan Fisik)"
                                            }
                                        ]
                                    },
                                    {
                                        "kondisi": "Pompa_GagalBerat = 1",
                                        "diagnosa": "Syok Kardiogenik"
                                    }
                                ]
                            },
                            {
                                "kondisi": "Hemo_Normal = 1",
                                "cabang": [
                                    {
                                        "kondisi": "Pompa_DisfungsiRingan = 0",
                                        "cabang": [
                                            {
                                                "kondisi": "Pompa_Normal = 0",
                                                "diagnosa": "Kebugaran Atletis (Prima)"
                                            },
                                            {
                                                "kondisi": "Pompa_Normal = 1",
                                                "diagnosa": "Normal / Sehat Terkontrol"
                                            }
                                        ]
                                    },
                                    {
                                        "kondisi": "Pompa_DisfungsiRingan = 1",
                                        "cabang": [
                                            {
                                                "kondisi": "Kardio_Ringan = 0",
                                                "cabang": [
                                                    {
                                                        "kondisi": "Beban_Tinggi = 0",
                                                        "diagnosa": "Disfungsi Diastolik Terisolasi"
                                                    },
                                                    {
                                                        "kondisi": "Beban_Tinggi = 1",
                                                        "diagnosa": "Kelelahan Otot Miokard"
                                                    }
                                                ]
                                            },
                                            {
                                                "kondisi": "Kardio_Ringan = 1",
                                                "diagnosa": "Gangguan Pompa Ringan (Mild HFrEF)"
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "kondisi": "Oksi_HipoksiaRingan = 1",
                        "cabang": [
                            {
                                "kondisi": "Hemo_Normal = 0",
                                "cabang": [
                                    {
                                        "kondisi": "Hemo_Syok = 0",
                                        "cabang": [
                                            {
                                                "kondisi": "Hemo_Krisis = 0",
                                                "cabang": [
                                                    {
                                                        "kondisi": "Pompa_GagalBerat = 0",
                                                        "diagnosa": "Gagal Jantung Kongestif Kanan"
                                                    },
                                                    {
                                                        "kondisi": "Pompa_GagalBerat = 1",
                                                        "cabang": [
                                                            {
                                                                "kondisi": "Beban_Tinggi = 0",
                                                                "diagnosa": "Kardiomiopati Dilatasi"
                                                            },
                                                            {
                                                                "kondisi": "Beban_Tinggi = 1",
                                                                "diagnosa": "Gagal Jantung Kongestif Kiri"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "kondisi": "Hemo_Krisis = 1",
                                                "diagnosa": "Obesitas Sentral Risiko Kardio"
                                            }
                                        ]
                                    },
                                    {
                                        "kondisi": "Hemo_Syok = 1",
                                        "cabang": [
                                            {
                                                "kondisi": "Pompa_DisfungsiRingan = 0",
                                                "diagnosa": "Iskemia Jaringan Perifer"
                                            },
                                            {
                                                "kondisi": "Pompa_DisfungsiRingan = 1",
                                                "diagnosa": "Bradikardia Simtomatik"
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "kondisi": "Hemo_Normal = 1",
                                "diagnosa": "Sleep Apnea Suspect (OSA)"
                            }
                        ]
                    }
                ]
            },
            {
                "kondisi": "Konduksi_Takiaritmia = 1",
                "cabang": [
                    {
                        "kondisi": "Oksi_GagalNapas = 0",
                        "cabang": [
                            {
                                "kondisi": "Pompa_DisfungsiRingan = 0",
                                "cabang": [
                                    {
                                        "kondisi": "Pompa_Hiper = 0",
                                        "cabang": [
                                            {
                                                "kondisi": "Pompa_Normal = 0",
                                                "cabang": [
                                                    {
                                                        "kondisi": "Hemo_Krisis = 0",
                                                        "cabang": [
                                                            {
                                                                "kondisi": "Pompa_GagalBerat = 0",
                                                                "diagnosa": "Takiaritmia Ventrikel Berbahaya"
                                                            },
                                                            {
                                                                "kondisi": "Pompa_GagalBerat = 1",
                                                                "diagnosa": "Risiko Henti Jantung (SCA)"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "kondisi": "Hemo_Krisis = 1",
                                                        "diagnosa": "Sindrom Koroner Akut (ACS)"
                                                    }
                                                ]
                                            },
                                            {
                                                "kondisi": "Pompa_Normal = 1",
                                                "cabang": [
                                                    {
                                                        "kondisi": "Hemo_Syok = 0",
                                                        "cabang": [
                                                            {
                                                                "kondisi": "Hemo_Krisis = 0",
                                                                "cabang": [
                                                                    {
                                                                        "kondisi": "Tol_IntoleransiBerat = 0",
                                                                        "diagnosa": "Takipnea Kronis (Sesak)"
                                                                    },
                                                                    {
                                                                        "kondisi": "Tol_IntoleransiBerat = 1",
                                                                        "diagnosa": "Infeksi Paru / Pneumonia"
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "kondisi": "Hemo_Krisis = 1",
                                                                "diagnosa": "Kecemasan Akut / Panic Attack"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "kondisi": "Hemo_Syok = 1",
                                                        "cabang": [
                                                            {
                                                                "kondisi": "Oksi_HipoksiaRingan = 0",
                                                                "diagnosa": "Hipotensi Ortostatik"
                                                            },
                                                            {
                                                                "kondisi": "Oksi_HipoksiaRingan = 1",
                                                                "diagnosa": "Syok Hipovolemik / Dehidrasi"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "kondisi": "Pompa_Hiper = 1",
                                        "diagnosa": "Kardiomiopati Hipertrofik"
                                    }
                                ]
                            },
                            {
                                "kondisi": "Pompa_DisfungsiRingan = 1",
                                "diagnosa": "Fibrilasi Atrium (AFib Suspect)"
                            }
                        ]
                    },
                    {
                        "kondisi": "Oksi_GagalNapas = 1",
                        "cabang": [
                            {
                                "kondisi": "Pompa_GagalBerat = 0",
                                "cabang": [
                                    {
                                        "kondisi": "Pompa_DisfungsiRingan = 0",
                                        "diagnosa": "Asfiksia Terinduksi Latihan"
                                    },
                                    {
                                        "kondisi": "Pompa_DisfungsiRingan = 1",
                                        "cabang": [
                                            {
                                                "kondisi": "Kardio_Ringan = 0",
                                                "diagnosa": "Hipoksia Jaringan Akut"
                                            },
                                            {
                                                "kondisi": "Kardio_Ringan = 1",
                                                "diagnosa": "Cor Pulmonale (Gagal Jantung Kanan)"
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "kondisi": "Pompa_GagalBerat = 1",
                                "cabang": [
                                    {
                                        "kondisi": "Beban_Tinggi = 0",
                                        "diagnosa": "Gagal Jantung Akut (AHF)"
                                    },
                                    {
                                        "kondisi": "Beban_Tinggi = 1",
                                        "diagnosa": "Edema Paru Kardiogenik"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]

    def mcu_ctrl_create(self):
        # inputnya di sini
        tensi_sys = ctrl.Antecedent(np.arange(0, 251, 1), 'tensi_sys')
        tensi_dia = ctrl.Antecedent(np.arange(0, 151, 1), 'tensi_dia')
        bmi       = ctrl.Antecedent(np.arange(10, 51, 0.1), 'bmi')
        rr        = ctrl.Antecedent(np.arange(0, 61, 1), 'rr')
        spo2      = ctrl.Antecedent(np.arange(50, 101, 1), 'spo2')
        hr        = ctrl.Antecedent(np.arange(30, 221, 1), 'hr')
        pr_int    = ctrl.Antecedent(np.arange(50, 301, 1), 'pr_int')
        qrs_dur   = ctrl.Antecedent(np.arange(50, 251, 1), 'qrs_dur')
        ctr       = ctrl.Antecedent(np.arange(20, 81, 1), 'ctr')
        ef        = ctrl.Antecedent(np.arange(10, 101, 1), 'ef')
        fs        = ctrl.Antecedent(np.arange(10, 61, 1), 'fs')
        lvidd     = ctrl.Antecedent(np.arange(20, 91, 1), 'lvidd')
        mets      = ctrl.Antecedent(np.arange(0, 21, 0.1), 'mets')
        max_hr    = ctrl.Antecedent(np.arange(0, 101, 1), 'max_hr')

        # buat outputnya
        hemo     = ctrl.Consequent(np.arange(0, 101, 1), 'hemo')
        pompa    = ctrl.Consequent(np.arange(0, 101, 1), 'pompa')
        konduksi = ctrl.Consequent(np.arange(0, 101, 1), 'konduksi')
        oksi     = ctrl.Consequent(np.arange(0, 101, 1), 'oksi')
        kardio   = ctrl.Consequent(np.arange(0, 101, 1), 'kardio')
        toleransi= ctrl.Consequent(np.arange(0, 101, 1), 'toleransi')
        meta     = ctrl.Consequent(np.arange(0, 101, 1), 'meta')
        beban    = ctrl.Consequent(np.arange(0, 101, 1), 'beban')
        efisien  = ctrl.Consequent(np.arange(0, 101, 1), 'efisien')
        aero     = ctrl.Consequent(np.arange(0, 101, 1), 'aero')
        perfusi  = ctrl.Consequent(np.arange(0, 101, 1), 'perfusi')
        stres    = ctrl.Consequent(np.arange(0, 101, 1), 'stres')

        # Buat Input Fuzzy

        # Tensi Sistolik
        tensi_sys['Rendah'] = fuzz.trapmf(tensi_sys.universe, [0, 0, 80, 90])
        tensi_sys['Normal'] = fuzz.trapmf(tensi_sys.universe, [85, 90, 120, 125])
        tensi_sys['Pra_Hipertensi'] = fuzz.trapmf(tensi_sys.universe, [120, 125, 139, 145])
        tensi_sys['Tinggi'] = fuzz.trapmf(tensi_sys.universe, [140, 150, 250, 250])

        # Tensi Diastolik
        tensi_dia['Rendah'] = fuzz.trapmf(tensi_dia.universe, [0, 0, 50, 60])
        tensi_dia['Normal'] = fuzz.trapmf(tensi_dia.universe, [55, 60, 80, 85])
        tensi_dia['Pra_Hipertensi'] = fuzz.trapmf(tensi_dia.universe, [80, 85, 89, 95])
        tensi_dia['Tinggi'] = fuzz.trapmf(tensi_dia.universe, [90, 100, 150, 150])

        # BMI
        bmi['Kurang'] = fuzz.trapmf(bmi.universe, [0, 0, 17, 18.5])
        bmi['Normal'] = fuzz.trapmf(bmi.universe, [17.5, 18.5, 24.9, 26])
        bmi['Berlebih'] = fuzz.trapmf(bmi.universe, [25, 26, 29.9, 31])
        bmi['Obesitas'] = fuzz.trapmf(bmi.universe, [30, 32, 50, 50])

        # Laju Pernapasan (RR)
        rr['Lambat'] = fuzz.trapmf(rr.universe, [0, 0, 10, 12])
        rr['Normal'] = fuzz.trapmf(rr.universe, [10, 12, 20, 22])
        rr['Cepat'] = fuzz.trapmf(rr.universe, [20, 24, 60, 60])

        # Saturasi Oksigen (SpO2)
        spo2['Hipoksia'] = fuzz.trapmf(spo2.universe, [0, 0, 85, 90])
        spo2['Waspada'] = fuzz.trapmf(spo2.universe, [88, 90, 94, 96])
        spo2['Normal'] = fuzz.trapmf(spo2.universe, [95, 96, 100, 100])

        # Heart Rate (HR)
        hr['Bradikardia'] = fuzz.trapmf(hr.universe, [0, 0, 50, 60])
        hr['Normal'] = fuzz.trapmf(hr.universe, [55, 60, 100, 105])
        hr['Takikardia'] = fuzz.trapmf(hr.universe, [100, 110, 220, 220])

        # PR Interval
        pr_int['Pendek'] = fuzz.trapmf(pr_int.universe, [0, 0, 100, 120])
        pr_int['Normal'] = fuzz.trapmf(pr_int.universe, [110, 120, 200, 210])
        pr_int['Memanjang'] = fuzz.trapmf(pr_int.universe, [200, 220, 300, 300])

        # QRS Duration
        qrs_dur['Normal'] = fuzz.trapmf(qrs_dur.universe, [0, 0, 100, 120])
        qrs_dur['Lebar'] = fuzz.trapmf(qrs_dur.universe, [110, 120, 250, 250])

        # Cardiothoracic Ratio (CTR)
        ctr['Normal'] = fuzz.trapmf(ctr.universe, [0, 0, 45, 50])
        ctr['Ringan'] = fuzz.trapmf(ctr.universe, [48, 50, 55, 58])
        ctr['Berat'] = fuzz.trapmf(ctr.universe, [55, 60, 100, 100])

        # Ejection Fraction (EF)
        ef['Lemah'] = fuzz.trapmf(ef.universe, [0, 0, 35, 40])
        ef['Waspada'] = fuzz.trapmf(ef.universe, [38, 40, 49, 52])
        ef['Normal'] = fuzz.trapmf(ef.universe, [50, 55, 70, 75])
        ef['Hiper'] = fuzz.trapmf(ef.universe, [72, 75, 100, 100])

        # Fractional Shortening (FS)
        fs['Menurun'] = fuzz.trapmf(fs.universe, [0, 0, 20, 25])
        fs['Normal'] = fuzz.trapmf(fs.universe, [20, 25, 100, 100])

        # LVIDd
        lvidd['Normal'] = fuzz.trapmf(lvidd.universe, [0, 0, 45, 53])
        lvidd['Membengkak'] = fuzz.trapmf(lvidd.universe, [50, 53, 100, 100])

        # Skor METs
        mets['Buruk'] = fuzz.trapmf(mets.universe, [0, 0, 4, 5])
        mets['Sedang'] = fuzz.trapmf(mets.universe, [4.5, 5, 8, 8.5])
        mets['Baik'] = fuzz.trapmf(mets.universe, [8, 9, 12, 12.5])
        mets['Sangat_Baik'] = fuzz.trapmf(mets.universe, [12, 13, 20, 20])

        # % Max HR Tercapai
        max_hr['Tidak_Maksimal'] = fuzz.trapmf(max_hr.universe, [0, 0, 75, 85])
        max_hr['Optimal'] = fuzz.trapmf(max_hr.universe, [80, 85, 100, 100])


        # Buat Output Fuzzy

        # Indeks Hemodinamik Dasar
        hemo['Syok'] = fuzz.trapmf(hemo.universe, [0, 0, 20, 40])
        hemo['Normal'] = fuzz.trapmf(hemo.universe, [30, 50, 70, 80])
        hemo['Krisis'] = fuzz.trapmf(hemo.universe, [70, 80, 100, 100])

        # Indeks Kinerja Pompa Jantung
        pompa['Gagal_Berat'] = fuzz.trapmf(pompa.universe, [0, 0, 25, 40])
        pompa['Disfungsi_Ringan'] = fuzz.trimf(pompa.universe, [30, 45, 60])
        pompa['Normal'] = fuzz.trapmf(pompa.universe, [50, 65, 80, 90])
        pompa['Hiper'] = fuzz.trapmf(pompa.universe, [80, 90, 100, 100])

        # Indeks Risiko Konduksi
        konduksi['Stabil'] = fuzz.trapmf(konduksi.universe, [0, 0, 20, 40])
        konduksi['Blok'] = fuzz.trapmf(konduksi.universe, [30, 40, 60, 70])
        konduksi['Takiaritmia'] = fuzz.trapmf(konduksi.universe, [60, 70, 85, 90])
        konduksi['Bradiaritmia'] = fuzz.trapmf(konduksi.universe, [85, 90, 100, 100])

        # Indeks Oksigenasi Paru
        oksi['Gagal_Napas'] = fuzz.trapmf(oksi.universe, [0, 0, 30, 50])
        oksi['Hipoksia_Ringan'] = fuzz.trimf(oksi.universe, [30, 60, 80])
        oksi['Normal'] = fuzz.trapmf(oksi.universe, [70, 80, 100, 100])

        # Indeks Kardiomegali Struktural
        kardio['Normal'] = fuzz.trapmf(kardio.universe, [0, 0, 30, 50])
        kardio['Ringan'] = fuzz.trimf(kardio.universe, [40, 60, 80])
        kardio['Masif'] = fuzz.trapmf(kardio.universe, [70, 80, 100, 100])

        # Indeks Toleransi Latihan
        toleransi['Intoleransi_Berat'] = fuzz.trapmf(toleransi.universe, [0, 0, 25, 40])
        toleransi['Kapasitas_Kurang'] = fuzz.trimf(toleransi.universe, [30, 55, 80])
        toleransi['Kapasitas_Baik'] = fuzz.trapmf(toleransi.universe, [70, 85, 100, 100])

        # Indeks Sindrom Metabolik
        meta['Normal'] = fuzz.trapmf(meta.universe, [0, 0, 30, 50])
        meta['Berisiko'] = fuzz.trimf(meta.universe, [40, 60, 80])
        meta['Sindrom_Metabolik'] = fuzz.trapmf(meta.universe, [70, 85, 100, 100])

        # Indeks Beban Kerja Miokardium
        beban['Rendah'] = fuzz.trapmf(beban.universe, [0, 0, 20, 35])
        beban['Optimal'] = fuzz.trapmf(beban.universe, [25, 40, 60, 75])
        beban['Tinggi'] = fuzz.trimf(beban.universe, [60, 80, 90])
        beban['Sangat_Tinggi'] = fuzz.trapmf(beban.universe, [80, 90, 100, 100])

        # Indeks Efisiensi Struktural
        efisien['Disfungsi_Parah'] = fuzz.trapmf(efisien.universe, [0, 0, 30, 50])
        efisien['Kompensasi'] = fuzz.trimf(efisien.universe, [30, 60, 85])
        efisien['Normal'] = fuzz.trapmf(efisien.universe, [75, 85, 100, 100])

        # Indeks Kapasitas Aerobik
        aero['Asfiksia_Latihan'] = fuzz.trapmf(aero.universe, [0, 0, 20, 40])
        aero['Kurang'] = fuzz.trimf(aero.universe, [30, 50, 70])
        aero['Prima'] = fuzz.trapmf(aero.universe, [60, 80, 100, 100])

        # Indeks Perfusi Jaringan
        perfusi['Iskemia'] = fuzz.trapmf(perfusi.universe, [0, 0, 30, 50])
        perfusi['Cukup'] = fuzz.trimf(perfusi.universe, [40, 60, 80])
        perfusi['Normal'] = fuzz.trapmf(perfusi.universe, [70, 85, 100, 100])

        # Indeks Stres Fisiologis
        stres['Rileks'] = fuzz.trapmf(stres.universe, [0, 0, 35, 55])
        stres['Tertekan'] = fuzz.trimf(stres.universe, [40, 65, 85])
        stres['Distres_Berat'] = fuzz.trapmf(stres.universe, [75, 85, 100, 100])

        # --- 1. Indeks Hemodinamik Dasar ---
        rule_hemo_1 = ctrl.Rule(tensi_sys['Rendah'] | tensi_dia['Rendah'], hemo['Syok'])
        rule_hemo_2 = ctrl.Rule(tensi_sys['Normal'] & tensi_dia['Normal'], hemo['Normal'])
        rule_hemo_3 = ctrl.Rule(tensi_sys['Pra_Hipertensi'] | tensi_dia['Pra_Hipertensi'], hemo['Normal'])
        rule_hemo_4 = ctrl.Rule(tensi_sys['Tinggi'] | tensi_dia['Tinggi'], hemo['Krisis'])

        # --- 2. Indeks Kinerja Pompa Jantung ---
        rule_pompa_1 = ctrl.Rule(ef['Lemah'] | fs['Menurun'], pompa['Gagal_Berat'])
        rule_pompa_2 = ctrl.Rule(ef['Waspada'] & fs['Normal'], pompa['Disfungsi_Ringan'])
        rule_pompa_3 = ctrl.Rule(ef['Normal'] & fs['Normal'], pompa['Normal'])
        rule_pompa_4 = ctrl.Rule(ef['Hiper'], pompa['Hiper'])

        # --- 3. Indeks Risiko Konduksi ---
        rule_konduksi_1 = ctrl.Rule(pr_int['Memanjang'] | qrs_dur['Lebar'], konduksi['Blok'])
        rule_konduksi_2 = ctrl.Rule(hr['Takikardia'] & pr_int['Normal'], konduksi['Takiaritmia'])
        rule_konduksi_3 = ctrl.Rule(hr['Bradikardia'] & pr_int['Normal'], konduksi['Bradiaritmia'])
        rule_konduksi_4 = ctrl.Rule(hr['Normal'] & pr_int['Normal'] & qrs_dur['Normal'], konduksi['Stabil'])

        # --- 4. Indeks Oksigenasi Paru ---
        rule_oksi_1 = ctrl.Rule(spo2['Hipoksia'] | (spo2['Waspada'] & rr['Cepat']), oksi['Gagal_Napas'])
        rule_oksi_2 = ctrl.Rule((spo2['Waspada'] & rr['Normal']) | (spo2['Normal'] & rr['Cepat']), oksi['Hipoksia_Ringan'])
        rule_oksi_3 = ctrl.Rule(spo2['Normal'] & rr['Normal'], oksi['Normal'])

        # --- 5. Indeks Kardiomegali Struktural ---
        rule_kardio_1 = ctrl.Rule(ctr['Berat'] | lvidd['Membengkak'], kardio['Masif'])
        rule_kardio_2 = ctrl.Rule(ctr['Ringan'] & lvidd['Normal'], kardio['Ringan'])
        rule_kardio_3 = ctrl.Rule(ctr['Normal'] & lvidd['Normal'], kardio['Normal'])

        # --- 6. Indeks Toleransi Latihan ---
        rule_tol_1 = ctrl.Rule(mets['Buruk'] | max_hr['Tidak_Maksimal'], toleransi['Intoleransi_Berat'])
        rule_tol_2 = ctrl.Rule(mets['Sedang'] & max_hr['Optimal'], toleransi['Kapasitas_Kurang'])
        rule_tol_3 = ctrl.Rule((mets['Baik'] | mets['Sangat_Baik']) & max_hr['Optimal'], toleransi['Kapasitas_Baik'])

        # --- 7. Indeks Sindrom Metabolik ---
        rule_meta_1 = ctrl.Rule(bmi['Obesitas'] & (tensi_sys['Tinggi'] | tensi_dia['Tinggi']), meta['Sindrom_Metabolik'])
        rule_meta_2 = ctrl.Rule(bmi['Berlebih'] | tensi_sys['Pra_Hipertensi'] | tensi_dia['Pra_Hipertensi'], meta['Berisiko'])
        rule_meta_3 = ctrl.Rule(bmi['Normal'] & tensi_sys['Normal'] & tensi_dia['Normal'], meta['Normal'])

        # --- 8. Indeks Beban Kerja Miokardium ---
        rule_beban_1 = ctrl.Rule(tensi_sys['Tinggi'] & hr['Takikardia'], beban['Sangat_Tinggi'])
        rule_beban_2 = ctrl.Rule(tensi_sys['Tinggi'] | hr['Takikardia'], beban['Tinggi'])
        rule_beban_3 = ctrl.Rule(tensi_sys['Normal'] & hr['Normal'], beban['Optimal'])
        rule_beban_4 = ctrl.Rule(tensi_sys['Rendah'] | hr['Bradikardia'], beban['Rendah'])

        # --- 9. Indeks Efisiensi Struktural ---
        rule_efisien_1 = ctrl.Rule(ef['Lemah'] & lvidd['Membengkak'], efisien['Disfungsi_Parah'])
        rule_efisien_2 = ctrl.Rule((ef['Lemah'] | ef['Waspada']) & lvidd['Normal'], efisien['Kompensasi'])
        rule_efisien_3 = ctrl.Rule((ef['Normal'] | ef['Hiper']) & lvidd['Normal'], efisien['Normal'])

        # --- 10. Indeks Kapasitas Aerobik ---
        rule_aero_1 = ctrl.Rule(rr['Cepat'] & mets['Buruk'], aero['Asfiksia_Latihan'])
        rule_aero_2 = ctrl.Rule(rr['Normal'] & mets['Buruk'], aero['Kurang'])
        rule_aero_3 = ctrl.Rule(rr['Normal'] & (mets['Baik'] | mets['Sangat_Baik']), aero['Prima'])

        # --- 11. Indeks Perfusi Jaringan ---
        rule_perfusi_1 = ctrl.Rule(tensi_dia['Rendah'] | spo2['Hipoksia'], perfusi['Iskemia'])
        rule_perfusi_2 = ctrl.Rule(tensi_dia['Tinggi'] | spo2['Waspada'], perfusi['Cukup'])
        rule_perfusi_3 = ctrl.Rule((tensi_dia['Normal'] | tensi_dia['Pra_Hipertensi']) & spo2['Normal'], perfusi['Normal'])

        # --- 12. Indeks Stres Fisiologis ---
        rule_stres_1 = ctrl.Rule(hr['Takikardia'] & rr['Cepat'], stres['Distres_Berat'])
        rule_stres_2 = ctrl.Rule(hr['Takikardia'] | rr['Cepat'], stres['Tertekan'])
        rule_stres_3 = ctrl.Rule((hr['Normal'] | hr['Bradikardia']) & (rr['Normal'] | rr['Lambat']), stres['Rileks'])


        # Daftarkan semua 40 aturan di atas ke dalam Control System
        mcu_ctrl = ctrl.ControlSystem([
            rule_hemo_1, rule_hemo_2, rule_hemo_3, rule_hemo_4,
            rule_pompa_1, rule_pompa_2, rule_pompa_3, rule_pompa_4,
            rule_konduksi_1, rule_konduksi_2, rule_konduksi_3, rule_konduksi_4,
            rule_oksi_1, rule_oksi_2, rule_oksi_3,
            rule_kardio_1, rule_kardio_2, rule_kardio_3,
            rule_tol_1, rule_tol_2, rule_tol_3,
            rule_meta_1, rule_meta_2, rule_meta_3,
            rule_beban_1, rule_beban_2, rule_beban_3, rule_beban_4,
            rule_efisien_1, rule_efisien_2, rule_efisien_3,
            rule_aero_1, rule_aero_2, rule_aero_3,
            rule_perfusi_1, rule_perfusi_2, rule_perfusi_3,
            rule_stres_1, rule_stres_2, rule_stres_3
        ])

        return mcu_ctrl