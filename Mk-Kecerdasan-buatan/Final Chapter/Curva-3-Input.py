import numpy as np
import matplotlib.pyplot as plt

# Fungsi keanggotaan segitiga
def triangular(x, a, b, c):
    return np.maximum(0, np.minimum((x - a) / (b - a), (c - x) / (c - b)))

# Fungsi keanggotaan trapesium
def trapezoidal(x, a, b, c, d):
    return np.maximum(0, np.minimum(np.minimum((x - a) / (b - a), 1), (d - x) / (d - c)))

# Fungsi shoulder kanan
def shoulder_right(x, a, b):
    return np.where(x <= a, 0, np.where(x >= b, 1, (x - a) / (b - a)))

# Setup plot
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle('KURVA FUNGSI KEANGGOTAAN FUZZY - SISTEM DETEKSI GEMPA', fontsize=16, fontweight='bold')

# ============================================================================
# 1. SKALA RICHTER (SR) - Kekuatan Gempa
# ============================================================================
x_sr = np.linspace(0, 8, 1000)

# Himpunan: RENDAH, SEDANG, TINGGI
rendah_sr = triangular(x_sr, 0, 2.5, 5.0)        # Segitiga [0, 2.5, 5.0]
sedang_sr = trapezoidal(x_sr, 3.0, 4.5, 5.5, 6.5) # Trapesium [3.0, 4.5, 5.5, 6.5]
tinggi_sr = shoulder_right(x_sr, 5.0, 7.0)       # Shoulder kanan [5.0, 7.0]

axes[0].plot(x_sr, rendah_sr, 'b-', linewidth=3, label='RENDAH')
axes[0].plot(x_sr, sedang_sr, 'g-', linewidth=3, label='SEDANG')
axes[0].plot(x_sr, tinggi_sr, 'r-', linewidth=3, label='TINGGI')
axes[0].set_title('SKALA RICHTER\nKekuatan Gempa', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Skala Richter')
axes[0].set_ylabel('Derajat Keanggotaan (μ)')
axes[0].legend(fontsize=12)
axes[0].grid(True, alpha=0.3)
axes[0].set_xlim(0, 8)

# Anotasi titik penting
axes[0].axvline(2.5, color='blue', linestyle='--', alpha=0.5)
axes[0].axvline(5.0, color='red', linestyle='--', alpha=0.5)
axes[0].text(2.5, 1.05, 'Puncak RENDAH', ha='center', fontsize=9, color='blue')
axes[0].text(5.0, 1.05, 'Batas RENDAH-TINGGI', ha='center', fontsize=9, color='red')

# ============================================================================
# 2. PERSENTASE DETEKSI (PD) - Jumlah Sensor yang Mendeteksi
# ============================================================================
x_pd = np.linspace(0, 100, 1000)

# Himpunan: SEDIKIT, CUKUP, BANYAK
sedikit_pd = triangular(x_pd, 0, 20, 40)         # Segitiga [0, 20, 40]
cukup_pd = trapezoidal(x_pd, 30, 45, 65, 80)     # Trapesium [30, 45, 65, 80]
banyak_pd = shoulder_right(x_pd, 60, 85)         # Shoulder kanan [60, 85]

axes[1].plot(x_pd, sedikit_pd, 'b-', linewidth=3, label='SEDIKIT')
axes[1].plot(x_pd, cukup_pd, 'g-', linewidth=3, label='CUKUP')
axes[1].plot(x_pd, banyak_pd, 'r-', linewidth=3, label='BANYAK')
axes[1].set_title('PERSENTASE DETEKSI\nJumlah Sensor yang Mendeteksi', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Persentase (%)')
axes[1].set_ylabel('Derajat Keanggotaan (μ)')
axes[1].legend(fontsize=12)
axes[1].grid(True, alpha=0.3)
axes[1].set_xlim(0, 100)

# Anotasi titik penting
axes[1].axvline(20, color='blue', linestyle='--', alpha=0.5)
axes[1].axvline(45, color='green', linestyle='--', alpha=0.5)
axes[1].axvline(65, color='green', linestyle='--', alpha=0.5)
axes[1].text(20, 1.05, 'Puncak SEDIKIT', ha='center', fontsize=9, color='blue')
axes[1].text(45, 1.05, 'Puncak CUKUP', ha='center', fontsize=9, color='green')

# ============================================================================
# 3. KONSISTENSI SINYAL (KS) - Kualitas dan Konsistensi Data
# ============================================================================
x_ks = np.linspace(0, 1, 1000)

# Himpunan: BURUK, BAIK, SANGAT_BAIK
buruk_ks = triangular(x_ks, 0, 0.2, 0.5)        # Segitiga [0, 0.2, 0.5]
baik_ks = trapezoidal(x_ks, 0.3, 0.5, 0.7, 0.8) # Trapesium [0.3, 0.5, 0.7, 0.8]
sangat_baik_ks = shoulder_right(x_ks, 0.6, 0.9) # Shoulder kanan [0.6, 0.9]

axes[2].plot(x_ks, buruk_ks, 'b-', linewidth=3, label='BURUK')
axes[2].plot(x_ks, baik_ks, 'g-', linewidth=3, label='BAIK')
axes[2].plot(x_ks, sangat_baik_ks, 'r-', linewidth=3, label='SANGAT BAIK')
axes[2].set_title('KONSISTENSI SINYAL\nKualitas dan Konsistensi Data', fontsize=14, fontweight='bold')
axes[2].set_xlabel('Index Konsistensi')
axes[2].set_ylabel('Derajat Keanggotaan (μ)')
axes[2].legend(fontsize=12)
axes[2].grid(True, alpha=0.3)
axes[2].set_xlim(0, 1)

# Anotasi titik penting
axes[2].axvline(0.2, color='blue', linestyle='--', alpha=0.5)
axes[2].axvline(0.5, color='green', linestyle='--', alpha=0.5)
axes[2].axvline(0.7, color='green', linestyle='--', alpha=0.5)
axes[2].text(0.2, 1.05, 'Puncak BURUK', ha='center', fontsize=9, color='blue')
axes[2].text(0.5, 1.05, 'Puncak BAIK', ha='center', fontsize=9, color='green')

# ============================================================================
# SIMPAN DAN TAMPILKAN
# ============================================================================
plt.tight_layout()
plt.subplots_adjust(top=0.85)


plt.show()

# ============================================================================
# CONTOH PERHITUNGAN DERAJAT KEANGGOTAAN
# ============================================================================
print("\n" + "="*70)
print("CONTOH PERHITUNGAN DERAJAT KEANGGOTAAN")
print("="*70)

# Contoh nilai input
contoh_sr = [3.0, 5.5, 7.0]
contoh_pd = [25.0, 50.0, 75.0]
contoh_ks = [0.3, 0.6, 0.9]

print("\n1. SKALA RICHTER:")
for sr in contoh_sr:
    μ_rendah = triangular(sr, 0, 2.5, 5.0)
    μ_sedang = trapezoidal(sr, 3.0, 4.5, 5.5, 6.5)
    μ_tinggi = shoulder_right(sr, 5.0, 7.0)
    print(f"   SR={sr}: RENDAH={μ_rendah:.3f}, SEDANG={μ_sedang:.3f}, TINGGI={μ_tinggi:.3f}")

print("\n2. PERSENTASE DETEKSI:")
for pd in contoh_pd:
    μ_sedikit = triangular(pd, 0, 20, 40)
    μ_cukup = trapezoidal(pd, 30, 45, 65, 80)
    μ_banyak = shoulder_right(pd, 60, 85)
    print(f"   PD={pd}%: SEDIKIT={μ_sedikit:.3f}, CUKUP={μ_cukup:.3f}, BANYAK={μ_banyak:.3f}")

print("\n3. KONSISTENSI SINYAL:")
for ks in contoh_ks:
    μ_buruk = triangular(ks, 0, 0.2, 0.5)
    μ_baik = trapezoidal(ks, 0.3, 0.5, 0.7, 0.8)
    μ_sangat_baik = shoulder_right(ks, 0.6, 0.9)
    print(f"   KS={ks}: BURUK={μ_buruk:.3f}, BAIK={μ_baik:.3f}, SANGAT_BAIK={μ_sangat_baik:.3f}")