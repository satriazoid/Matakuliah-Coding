import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import pandas as pd

# --- 1. Definisikan variabel ---
suhu = ctrl.Antecedent(np.arange(0, 101, 1), 'suhu')
kelembaban = ctrl.Antecedent(np.arange(0, 101, 1), 'kelembaban')
heater = ctrl.Consequent(np.arange(0, 256, 1), 'heater')
kipas = ctrl.Consequent(np.arange(0, 256, 1), 'kipas')

# --- 2. Fungsi keanggotaan (sesuai jurnal) ---
# Suhu
suhu['Dingin'] = fuzz.trapmf(suhu.universe, [0, 0, 15, 24])
suhu['Normal'] = fuzz.trapmf(suhu.universe, [15, 24, 27, 37])
suhu['Panas'] = fuzz.trapmf(suhu.universe, [24, 37, 100, 100])

# Kelembaban
kelembaban['Kering'] = fuzz.trapmf(kelembaban.universe, [0, 0, 43, 47])
kelembaban['Normal'] = fuzz.trapmf(kelembaban.universe, [43, 47, 59, 63])
kelembaban['Basah'] = fuzz.trapmf(kelembaban.universe, [59, 63, 100, 100])

# Heater
heater['Normal'] = fuzz.trapmf(heater.universe, [0, 0, 72, 95])
heater['Hangat'] = fuzz.trapmf(heater.universe, [72, 95, 117, 140])
heater['Panas'] = fuzz.trapmf(heater.universe, [117, 140, 225, 225])

# Kipas
kipas['Lambat'] = fuzz.trapmf(kipas.universe, [0, 0, 72, 94.5])
kipas['Normal'] = fuzz.trapmf(kipas.universe, [72, 95, 117, 140])
kipas['Cepat'] = fuzz.trapmf(kipas.universe, [117, 140, 225, 225])

# --- 3. Aturan Fuzzy (10 rules) ---
rule1 = ctrl.Rule(kelembaban['Kering'] & suhu['Dingin'], [kipas['Lambat'], heater['Hangat']])
rule2 = ctrl.Rule(kelembaban['Kering'] & suhu['Normal'], [kipas['Normal'], heater['Normal']])
rule3 = ctrl.Rule(kelembaban['Kering'] & suhu['Panas'], kipas['Cepat'])  # heater tidak disebut → default?
rule4 = ctrl.Rule(kelembaban['Normal'] & suhu['Dingin'], [kipas['Lambat'], heater['Hangat']])
rule5 = ctrl.Rule(kelembaban['Normal'] & suhu['Normal'], [kipas['Normal'], heater['Normal']])
rule6 = ctrl.Rule(kelembaban['Normal'] & suhu['Panas'], [kipas['Cepat'], heater['Normal']])
rule7 = ctrl.Rule(kelembaban['Basah'] & suhu['Dingin'], [kipas['Cepat'], heater['Panas']])
rule8 = ctrl.Rule(kelembaban['Basah'] & suhu['Normal'], [kipas['Normal'], heater['Panas']])
rule9 = ctrl.Rule(kelembaban['Basah'] & suhu['Panas'], [kipas['Cepat'], heater['Hangat']])
# Rule 10 duplikat rule9 → abaikan

# --- 4. Sistem kontrol ---
sistem = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
sim = ctrl.ControlSystemSimulation(sistem)

# --- 5. Simulasi database ---
data = []
for t in range(15, 51):          # suhu 15–50
    for h in range(30, 81, 5):   # kelembaban 30–80
        try:
            sim.input['suhu'] = t
            sim.input['kelembaban'] = h
            sim.compute()
            heater_val = sim.output['heater']
            kipas_val = sim.output['kipas']
            data.append([t, h, heater_val, kipas_val])
        except Exception as e:
            # Jika aturan tidak mencakup, isi dengan NaN atau estimasi
            data.append([t, h, np.nan, np.nan])

# Simpan ke CSV
df = pd.DataFrame(data, columns=['suhu', 'kelembaban', 'heater_pwm', 'kipas_pwm'])
print(df.head())