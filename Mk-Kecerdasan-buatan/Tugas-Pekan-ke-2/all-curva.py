import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

# --- 1. Input: SUHU (0–100°C) ---
x_suhu = np.arange(0, 101, 1)
suhu_dingin = fuzz.trapmf(x_suhu, [0, 0, 15, 24])
suhu_normal = fuzz.trapmf(x_suhu, [15, 24, 27, 37])
suhu_panas  = fuzz.trapmf(x_suhu, [24, 37, 100, 100])

# --- 2. Input: KELEMBABAN (0–100%) ---
x_hum = np.arange(0, 101, 1)
hum_kering = fuzz.trapmf(x_hum, [0, 0, 43, 47])
hum_normal = fuzz.trapmf(x_hum, [43, 47, 59, 63])
hum_basah  = fuzz.trapmf(x_hum, [59, 63, 100, 100])

# --- 3. Output: HEATER & KIPAS (0–255 PWM) ---
x_pwm = np.arange(0, 256, 1)

# Heater
heater_normal = fuzz.trapmf(x_pwm, [0, 0, 72, 95])
heater_hangat = fuzz.trapmf(x_pwm, [72, 95, 117, 140])
heater_panas  = fuzz.trapmf(x_pwm, [117, 140, 225, 225])

# Kipas
kipas_lambat = fuzz.trapmf(x_pwm, [0, 0, 72, 94.5])
kipas_normal = fuzz.trapmf(x_pwm, [72, 95, 117, 140])
kipas_cepat  = fuzz.trapmf(x_pwm, [117, 140, 225, 225])

# --- Plot Semua ---
plt.figure(figsize=(16, 10))

# Suhu
plt.subplot(2, 2, 1)
plt.plot(x_suhu, suhu_dingin, 'b', linewidth=2, label='Dingin')
plt.plot(x_suhu, suhu_normal, 'g', linewidth=2, label='Normal')
plt.plot(x_suhu, suhu_panas,  'r', linewidth=2, label='Panas')
plt.title('Fungsi Keanggotaan: Suhu (Input)')
plt.xlabel('Suhu (°C)')
plt.ylabel('μ')
plt.legend()
plt.grid(True)
plt.xlim(0, 50)
plt.ylim(0, 1.1)
plt.plot(0, 1, 'bo')  # titik μ=1 di x=0

# Kelembaban
plt.subplot(2, 2, 2)
plt.plot(x_hum, hum_kering, 'b', linewidth=2, label='Kering')
plt.plot(x_hum, hum_normal, 'g', linewidth=2, label='Normal')
plt.plot(x_hum, hum_basah,  'r', linewidth=2, label='Basah')
plt.title('Fungsi Keanggotaan: Kelembaban (Input)')
plt.xlabel('Kelembaban (%)')
plt.ylabel('μ')
plt.legend()
plt.grid(True)
plt.xlim(0, 100)
plt.ylim(0, 1.1)
plt.plot(0, 1, 'bo')  # titik μ=1 di x=0

# Heater
plt.subplot(2, 2, 3)
plt.plot(x_pwm, heater_normal, 'b', linewidth=2, label='Normal')
plt.plot(x_pwm, heater_hangat, 'g', linewidth=2, label='Hangat')
plt.plot(x_pwm, heater_panas,  'r', linewidth=2, label='Panas')
plt.title('Fungsi Keanggotaan: Heater (Output PWM)')
plt.xlabel('PWM (0–255)')
plt.ylabel('μ')
plt.legend()
plt.grid(True)
plt.xlim(0, 255)
plt.ylim(0, 1.1)
plt.plot(0, 1, 'bo')  # μ=1 di PWM=0 → "Normal"

# Kipas
plt.subplot(2, 2, 4)
plt.plot(x_pwm, kipas_lambat, 'b', linewidth=2, label='Lambat')
plt.plot(x_pwm, kipas_normal, 'g', linewidth=2, label='Normal')
plt.plot(x_pwm, kipas_cepat,  'r', linewidth=2, label='Cepat')
plt.title('Fungsi Keanggotaan: Kipas (Output PWM)')
plt.xlabel('PWM (0–255)')
plt.ylabel('μ')
plt.legend()
plt.grid(True)
plt.xlim(0, 255)
plt.ylim(0, 1.1)
plt.plot(0, 1, 'bo')  # μ=1 di PWM=0 → "Lambat"

plt.tight_layout()
plt.show()