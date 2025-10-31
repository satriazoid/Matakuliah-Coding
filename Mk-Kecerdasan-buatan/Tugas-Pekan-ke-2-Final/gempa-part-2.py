import numpy as np
import matplotlib.pyplot as plt

# --- 1. Klarifikasi Angka Skala (Domain dan Semesta Pembicaraan) ---
# Skala pada sumbu X untuk SR adalah nilai Skala Richter (SR).
# Skala pada sumbu X untuk PS adalah nilai Persentase (%).

# --- 2. Definisi Fungsi Keanggotaan (Membership Functions) ---

# A. Kekuatan Gempa (SR)
def mu_sr_low(sr):
    # Turun: 4.0 ke 5.0
    if sr <= 4.0:
        return 1.0
    elif 4.0 < sr <= 5.0:
        return (5.0 - sr) / (5.0 - 4.0)
    else:
        return 0.0

def mu_sr_medium(sr):
    # Naik: 4.0 ke 5.0; Plateau: 5.0 ke 5.8; Turun: 5.8 ke 6.2
    if 4.0 < sr <= 5.0:
        return (sr - 4.0) / (5.0 - 4.0)
    elif 5.0 < sr <= 5.8:
        return 1.0
    elif 5.8 < sr <= 6.2:
        return (6.2 - sr) / (6.2 - 5.8)
    else:
        return 0.0

def mu_sr_high(sr):
    # Naik: 5.8 ke 6.2
    if 5.8 < sr <= 6.2:
        return (sr - 5.8) / (6.2 - 5.8)
    elif sr > 6.2:
        return 1.0
    else:
        return 0.0

# B. Persentase Sinyal (PS)
def mu_ps_sedikit(ps):
    # Turun: 35.0 ke 45.0
    if ps <= 35.0:
        return 1.0
    elif 35.0 < ps <= 45.0:
        return (45.0 - ps) / (45.0 - 35.0)
    else:
        return 0.0

def mu_ps_cukup(ps):
    # Naik: 35.0 ke 45.0; Plateau: 45.0 ke 55.0; Turun: 55.0 ke 75.0
    if 35.0 < ps <= 45.0:
        return (ps - 35.0) / (45.0 - 35.0)
    elif 45.0 < ps <= 55.0:
        return 1.0
    elif 55.0 < ps <= 75.0:
        return (75.0 - ps) / (75.0 - 55.0)
    else:
        return 0.0

def mu_ps_banyak(ps):
    # Naik: 55.0 ke 75.0
    if 55.0 < ps <= 75.0:
        return (ps - 55.0) / (75.0 - 55.0)
    elif ps > 75.0:
        return 1.0
    else:
        return 0.0

# --- 3. Visualisasi Kurva Keanggotaan ---

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
sr_range = np.arange(0, 8.1, 0.1)
ps_range = np.arange(0, 100.1, 1)

# Plot SR
axes[0].plot(sr_range, [mu_sr_low(x) for x in sr_range], 'b', label='LOW (SR)')
axes[0].plot(sr_range, [mu_sr_medium(x) for x in sr_range], 'g', label='MEDIUM (SR)')
axes[0].plot(sr_range, [mu_sr_high(x) for x in sr_range], 'r', label='HIGH (SR)')
axes[0].set_title('Kurva Keanggotaan Kekuatan Gempa (SR)')
axes[0].set_xlabel('Skala Richter (SR)')
axes[0].set_ylabel('Derajat Keanggotaan ($\mu$)')
axes[0].legend()
axes[0].grid(True, linestyle='--', alpha=0.6)

# Plot PS
axes[1].plot(ps_range, [mu_ps_sedikit(x) for x in ps_range], 'b', label='SEDIKIT (PS)')
axes[1].plot(ps_range, [mu_ps_cukup(x) for x in ps_range], 'g', label='CUKUP (PS)')
axes[1].plot(ps_range, [mu_ps_banyak(x) for x in ps_range], 'r', label='BANYAK (PS)')
axes[1].set_title('Kurva Keanggotaan Persentase Sinyal (PS)')
axes[1].set_xlabel('Persentase Sinyal (%)')
axes[1].set_ylabel('Derajat Keanggotaan ($\mu$)')
axes[1].legend()
axes[1].grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()

# --- 4. Simulasi Inferensi (Mencari Nilai Output Fuzzy) ---

# Aturan Inferensi (IF-THEN) dari Jurnal untuk Output "Gempa Valid (TRUE)"
# Menggunakan operator MIN (AND) pada premis (input).

# Aturan untuk TRUE:
# 1. IF SR HIGH AND PS BANYAK THEN TRUE
# 2. IF SR MEDIUM AND PS BANYAK THEN TRUE
# 3. IF SR HIGH AND PS CUKUP THEN TRUE

# Aturan untuk FALSE:
# Semua kombinasi lain menghasilkan FALSE, seperti:
# 4. IF SR LOW AND PS SEDIKIT THEN FALSE
# 5. IF SR MEDIUM AND PS SEDIKIT THEN FALSE
# 6. IF SR LOW AND PS BANYAK THEN FALSE (etc.)

def inferensi_fuzzy(sr_input, ps_input):
    # Fuzzifikasi Input
    mu_sr = {
        'LOW': mu_sr_low(sr_input),
        'MEDIUM': mu_sr_medium(sr_input),
        'HIGH': mu_sr_high(sr_input)
    }
    mu_ps = {
        'SEDIKIT': mu_ps_sedikit(ps_input),
        'CUKUP': mu_ps_cukup(ps_input),
        'BANYAK': mu_ps_banyak(ps_input)
    }

    # Inferensi (Menghitung nilai alpha-predikat untuk output TRUE)
    # Menggunakan operator MIN untuk AND
    alpha_true_1 = min(mu_sr['HIGH'], mu_ps['BANYAK'])
    alpha_true_2 = min(mu_sr['MEDIUM'], mu_ps['BANYAK'])
    alpha_true_3 = min(mu_sr['HIGH'], mu_ps['CUKUP'])

    # Agregasi (Mencari nilai keanggotaan tertinggi untuk output TRUE)
    # Menggunakan operator MAX (OR)
    mu_output_true = max(alpha_true_1, alpha_true_2, alpha_true_3)
    
    # Inferensi untuk output FALSE (Semua aturan lain, kita asumsikan 1-mu_output_true jika Mamdani)
    # Dalam kasus ini, output adalah kategori biner (TRUE/FALSE)
    
    return mu_output_true, mu_sr, mu_ps

# --- 5. Contoh Hasil Perhitungan (Output) ---

print("--- Hasil Simulasi Fuzzy Logic ---")

# Contoh 1: Gempa Kuat dan Banyak Sinyal (Harusnya TRUE)
SR_1 = 6.0
PS_1 = 80.0
mu_out_1, mu_sr_1, mu_ps_1 = inferensi_fuzzy(SR_1, PS_1)

print(f"\nContoh 1: Input SR={SR_1}, PS={PS_1}%")
print(f"  SR: LOW={mu_sr_1['LOW']:.2f}, MEDIUM={mu_sr_1['MEDIUM']:.2f}, HIGH={mu_sr_1['HIGH']:.2f}")
print(f"  PS: SEDIKIT={mu_ps_1['SEDIKIT']:.2f}, CUKUP={mu_ps_1['CUKUP']:.2f}, BANYAK={mu_ps_1['BANYAK']:.2f}")
print(f"  Nilai Keanggotaan Output TRUE (Valid): {mu_out_1:.4f}")
print(f"  Kesimpulan: {'Gempa Dinyatakan VALID (Peringatan Diberikan)' if mu_out_1 > 0 else 'Gempa Dinyatakan TIDAK VALID'}")

# Contoh 2: Gempa Lemah dan Sinyal Sedikit (Harusnya FALSE)
SR_2 = 4.2
PS_2 = 30.0
mu_out_2, mu_sr_2, mu_ps_2 = inferensi_fuzzy(SR_2, PS_2)

print(f"\nContoh 2: Input SR={SR_2}, PS={PS_2}%")
print(f"  SR: LOW={mu_sr_2['LOW']:.2f}, MEDIUM={mu_sr_2['MEDIUM']:.2f}, HIGH={mu_sr_2['HIGH']:.2f}")
print(f"  PS: SEDIKIT={mu_ps_2['SEDIKIT']:.2f}, CUKUP={mu_ps_2['CUKUP']:.2f}, BANYAK={mu_ps_2['BANYAK']:.2f}")
print(f"  Nilai Keanggotaan Output TRUE (Valid): {mu_out_2:.4f}")
print(f"  Kesimpulan: {'Gempa Dinyatakan VALID (Peringatan Diberikan)' if mu_out_2 > 0 else 'Gempa Dinyatakan TIDAK VALID'}")