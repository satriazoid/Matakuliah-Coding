import numpy as np
import matplotlib.pyplot as plt

# 1. FUNGSI KEANGGOTAAN UNTUK SKALA RICHTER
def richter_membership(x):
    # Definisi range untuk setiap himpunan fuzzy
    low = np.zeros_like(x)
    medium = np.zeros_like(x)
    high = np.zeros_like(x)
    
    # Himpunan LOW (Rendah)
    low[(x >= 0) & (x <= 4.0)] = 1.0
    low[(x > 4.0) & (x < 5.0)] = (5.0 - x[(x > 4.0) & (x < 5.0)]) / (5.0 - 4.0)
    
    # Himpunan MEDIUM (Sedang)
    medium[(x >= 4.0) & (x <= 5.0)] = (x[(x >= 4.0) & (x <= 5.0)] - 4.0) / (5.0 - 4.0)
    medium[(x > 5.0) & (x < 5.8)] = 1.0
    medium[(x >= 5.8) & (x <= 6.2)] = (6.2 - x[(x >= 5.8) & (x <= 6.2)]) / (6.2 - 5.8)
    
    # Himpunan HIGH (Tinggi)
    high[(x >= 5.8) & (x <= 6.2)] = (x[(x >= 5.8) & (x <= 6.2)] - 5.8) / (6.2 - 5.8)
    high[x >= 6.2] = 1.0
    
    return low, medium, high

# 2. FUNGSI KEANGGOTAAN UNTUK PERSENTASE SINYAL
def signal_membership(x):
    # Definisi range untuk setiap himpunan fuzzy
    sedikit = np.zeros_like(x)
    cukup = np.zeros_like(x)
    banyak = np.zeros_like(x)
    
    # Himpunan SEDIKIT
    sedikit[(x >= 0) & (x <= 35.0)] = 1.0
    sedikit[(x > 35.0) & (x < 45.0)] = (45.0 - x[(x > 35.0) & (x < 45.0)]) / (45.0 - 35.0)
    
    # Himpunan CUKUP
    cukup[(x >= 35.0) & (x <= 45.0)] = (x[(x >= 35.0) & (x <= 45.0)] - 35.0) / (45.0 - 35.0)
    cukup[(x > 45.0) & (x < 55.0)] = 1.0
    cukup[(x >= 55.0) & (x <= 75.0)] = (75.0 - x[(x >= 55.0) & (x <= 75.0)]) / (75.0 - 55.0)
    
    # Himpunan BANYAK
    banyak[(x >= 55.0) & (x <= 75.0)] = (x[(x >= 55.0) & (x <= 75.0)] - 55.0) / (75.0 - 55.0)
    banyak[x >= 75.0] = 1.0
    
    return sedikit, cukup, banyak

# 3. PLOT KURVA SKALA RICHTER
x_richter = np.linspace(0, 8, 1000)
low_r, medium_r, high_r = richter_membership(x_richter)

plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(x_richter, low_r, 'b', label='LOW', linewidth=2)
plt.plot(x_richter, medium_r, 'g', label='MEDIUM', linewidth=2)
plt.plot(x_richter, high_r, 'r', label='HIGH', linewidth=2)
plt.title('Fungsi Keanggotaan - Skala Richter')
plt.xlabel('Skala Richter')
plt.ylabel('Derajat Keanggotaan')
plt.legend()
plt.grid(True)

# 4. PLOT KURVA PERSENTASE SINYAL
x_signal = np.linspace(0, 100, 1000)
sedikit_s, cukup_s, banyak_s = signal_membership(x_signal)

plt.subplot(1, 2, 2)
plt.plot(x_signal, sedikit_s, 'b', label='SEDIKIT', linewidth=2)
plt.plot(x_signal, cukup_s, 'g', label='CUKUP', linewidth=2)
plt.plot(x_signal, banyak_s, 'r', label='BANYAK', linewidth=2)
plt.title('Fungsi Keanggotaan - Persentase Sinyal')
plt.xlabel('Persentase Sinyal (%)')
plt.ylabel('Derajat Keanggotaan')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# 5. CONTOH PERHITUNGAN DERAJAT KEANGGOTAAN
print("=== CONTOH PERHITUNGAN ===")
print("\n1. Untuk Skala Richter 4.5:")
low, med, high = richter_membership(np.array([4.5]))
print(f"   LOW: {low[0]:.3f}, MEDIUM: {med[0]:.3f}, HIGH: {high[0]:.3f}")

print("\n2. Untuk Skala Richter 6.0:")
low, med, high = richter_membership(np.array([6.0]))
print(f"   LOW: {low[0]:.3f}, MEDIUM: {med[0]:.3f}, HIGH: {high[0]:.3f}")

print("\n3. Untuk Persentase Sinyal 40%:")
sed, ckp, bnyk = signal_membership(np.array([40.0]))
print(f"   SEDIKIT: {sed[0]:.3f}, CUKUP: {ckp[0]:.3f}, BANYAK: {bnyk[0]:.3f}")

print("\n4. Untuk Persentase Sinyal 65%:")
sed, ckp, bnyk = signal_membership(np.array([65.0]))
print(f"   SEDIKIT: {sed[0]:.3f}, CUKUP: {ckp[0]:.3f}, BANYAK: {bnyk[0]:.3f}")