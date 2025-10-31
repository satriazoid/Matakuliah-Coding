import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

# --- 2. Input: KELEMBABAN (0–100%) ---
x_hum = np.arange(0, 101, 1)
hum_kering = fuzz.trapmf(x_hum, [0, 0, 43, 47])
hum_normal = fuzz.trapmf(x_hum, [43, 47, 59, 63])
hum_basah  = fuzz.trapmf(x_hum, [59, 63, 100, 100])

# --- Plot Semua ---
plt.figure(figsize=(16, 10))

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

plt.tight_layout()
plt.show()