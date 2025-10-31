import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random

# ==============================
# 1. FUNGSI KEANGGOTAAN MANUAL
# ==============================

def trapmf(x, a, b, c, d):
    """Fungsi keanggotaan trapesium"""
    if x <= a:
        return 0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x <= c:
        return 1
    elif c < x <= d:
        return (d - x) / (d - c)
    else:
        return 0

def fuzzifikasi_skala_richter(sr):
    """Mengembalikan label fuzzy dan derajat keanggotaan"""
    low = trapmf(sr, 0, 0, 4.0, 5.0)
    medium = trapmf(sr, 4.0, 5.0, 5.8, 6.2)
    high = trapmf(sr, 5.8, 6.2, 8, 8)
    
    # Pilih label dominan (max)
    max_val = max(low, medium, high)
    if max_val == low:
        return "LOW", low
    elif max_val == medium:
        return "MEDIUM", medium
    else:
        return "HIGH", high

def fuzzifikasi_persentase(ps):
    """Mengembalikan label fuzzy dan derajat keanggotaan"""
    sedikit = trapmf(ps, 0, 0, 35, 45)
    cukup = trapmf(ps, 35, 45, 55, 75)
    banyak = trapmf(ps, 55, 75, 100, 100)
    
    max_val = max(sedikit, cukup, banyak)
    if max_val == sedikit:
        return "SEDIKIT", sedikit
    elif max_val == cukup:
        return "CUKUP", cukup
    else:
        return "BANYAK", banyak

# ==============================
# 2. ATURAN FUZZY (Tabel III)
# ==============================

def inferensi_fuzzy(label_sr, label_ps):
    """Mengembalikan keputusan akhir: TRUE/FALSE"""
    # Tabel keanggotaan (Tabel III)
    tabel = {
        "SEDIKIT": {"LOW": False, "MEDIUM": False, "HIGH": False},
        "CUKUP":   {"LOW": False, "MEDIUM": True,  "HIGH": True},
        "BANYAK":  {"LOW": True,  "MEDIUM": True,  "HIGH": True}
    }
    return tabel[label_ps][label_sr]

# ==============================
# 3. GENERASI DATASET SIMULASI
# ==============================

data = []
for _ in range(500):
    sr = round(random.uniform(2.0, 7.5), 2)  # Skala Richter realistis
    ps = round(random.uniform(10, 95), 1)    # Persentase node aktif
    
    label_sr, _ = fuzzifikasi_skala_richter(sr)
    label_ps, _ = fuzzifikasi_persentase(ps)
    keputusan = inferensi_fuzzy(label_sr, label_ps)
    
    data.append([sr, ps, keputusan])

df = pd.DataFrame(data, columns=["skala_richter", "persentase_node_aktif", "keputusan"])
df.to_csv("gempa_fuzzy_dataset.csv", index=False)
print("✅ Dataset disimpan sebagai 'gempa_fuzzy_dataset.csv'")
print(df.head())

# ==============================
# 4. PLOT KURVA FUNGSI KEANGGOTAAN
# ==============================

# Domain
x_sr = np.linspace(0, 8, 400)
x_ps = np.linspace(0, 100, 400)

# Skala Richter
low_vals = [trapmf(x, 0, 0, 4.0, 5.0) for x in x_sr]
medium_vals = [trapmf(x, 4.0, 5.0, 5.8, 6.2) for x in x_sr]
high_vals = [trapmf(x, 5.8, 6.2, 8, 8) for x in x_sr]

# Persentase Node
sedikit_vals = [trapmf(x, 0, 0, 35, 45) for x in x_ps]
cukup_vals = [trapmf(x, 35, 45, 55, 75) for x in x_ps]
banyak_vals = [trapmf(x, 55, 75, 100, 100) for x in x_ps]

# Plot
plt.figure(figsize=(14, 6))

# Skala Richter
plt.subplot(1, 2, 1)
plt.plot(x_sr, low_vals, 'b', label='LOW')
plt.plot(x_sr, medium_vals, 'g', label='MEDIUM')
plt.plot(x_sr, high_vals, 'r', label='HIGH')
plt.title('Fungsi Keanggotaan: Skala Richter')
plt.xlabel('Skala Richter')
plt.ylabel('Derajat Keanggotaan (μ)')
plt.legend()
plt.grid(True)
plt.xlim(0, 8)
plt.ylim(0, 1.1)
plt.plot(0, 1, 'bo')  # μ=1 di x=0

# Persentase Node
plt.subplot(1, 2, 2)
plt.plot(x_ps, sedikit_vals, 'b', label='SEDIKIT')
plt.plot(x_ps, cukup_vals, 'g', label='CUKUP')
plt.plot(x_ps, banyak_vals, 'r', label='BANYAK')
plt.title('Fungsi Keanggotaan: Persentase Node Aktif')
plt.xlabel('Persentase (%)')
plt.ylabel('Derajat Keanggotaan (μ)')
plt.legend()
plt.grid(True)
plt.xlim(0, 100)
plt.ylim(0, 1.1)
plt.plot(0, 1, 'bo')  # μ=1 di x=0

plt.tight_layout()
plt.savefig("gempa_fuzzy_curves.png", dpi=300)
plt.show()
print("✅ Kurva disimpan sebagai 'gempa_fuzzy_curves.png'")