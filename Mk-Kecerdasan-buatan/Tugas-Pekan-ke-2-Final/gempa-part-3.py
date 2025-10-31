import numpy as np
import matplotlib.pyplot as plt

# --- 1. Definisi Fungsi Keanggotaan (Membership Functions) ---

# A. Kekuatan Gempa (SR: Skala Richter)
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

# B. Persentase Sinyal (PS: Persentase)
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

# --- 2. Visualisasi Kurva Keanggotaan ---

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
sr_range = np.arange(0, 8.1, 0.1)
ps_range = np.arange(0, 100.1, 1)

# Plot SR
axes[0].plot(sr_range, [mu_sr_low(x) for x in sr_range], 'b', label='LOW (SR)')
axes[0].plot(sr_range, [mu_sr_medium(x) for x in sr_range], 'g', label='MEDIUM (SR)')
axes[0].plot(sr_range, [mu_sr_high(x) for x in sr_range], 'r', label='HIGH (SR)')
axes[0].set_title('Kurva Keanggotaan Kekuatan Gempa')
axes[0].set_xlabel('Skala Richter (SR)')
axes[0].set_ylabel('Derajat Keanggotaan ($\mu$)')
axes[0].legend()
axes[0].grid(True, linestyle='--', alpha=0.6)

# Plot PS
axes[1].plot(ps_range, [mu_ps_sedikit(x) for x in ps_range], 'b', label='SEDIKIT (PS)')
axes[1].plot(ps_range, [mu_ps_cukup(x) for x in ps_range], 'g', label='CUKUP (PS)')
axes[1].plot(ps_range, [mu_ps_banyak(x) for x in ps_range], 'r', label='BANYAK (PS)')
axes[1].set_title('Kurva Keanggotaan Persentase Sinyal')
axes[1].set_xlabel('Persentase Sinyal (%)')
axes[1].set_ylabel('Derajat Keanggotaan ($\mu$)')
axes[1].legend()
axes[1].grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()

# --- 3. Contoh Hasil Perhitungan (Inferensi) ---

def inferensi_fuzzy(sr_input, ps_input):
    # Fuzzifikasi
    mu_sr = {
        'HIGH': mu_sr_high(sr_input),
        'MEDIUM': mu_sr_medium(sr_input),
    }
    mu_ps = {
        'BANYAK': mu_ps_banyak(ps_input),
        'CUKUP': mu_ps_cukup(ps_input),
    }

    # Inferensi (Aturan untuk Output TRUE) menggunakan MIN (AND)
    alpha_true_1 = min(mu_sr['HIGH'], mu_ps['BANYAK']) # IF HIGH AND BANYAK THEN TRUE
    alpha_true_2 = min(mu_sr['MEDIUM'], mu_ps['BANYAK']) # IF MEDIUM AND BANYAK THEN TRUE
    alpha_true_3 = min(mu_sr['HIGH'], mu_ps['CUKUP']) # IF HIGH AND CUKUP THEN TRUE

    # Agregasi (Mencari nilai keanggotaan tertinggi untuk output TRUE) menggunakan MAX (OR)
    mu_output_true = max(alpha_true_1, alpha_true_2, alpha_true_3)
    
    return mu_output_true

SR_TEST = 6.0
PS_TEST = 80.0
mu_out_test = inferensi_fuzzy(SR_TEST, PS_TEST)

print("\n--- Hasil Perhitungan Inferensi Contoh ---")
print(f"Input: SR={SR_TEST}, PS={PS_TEST}%")
print(f"Nilai Keanggotaan Output TRUE (Gempa Valid): {mu_out_test:.4f}")
print(f"Keputusan Sistem: {'VALID' if mu_out_test > 0 else 'TIDAK VALID'}")