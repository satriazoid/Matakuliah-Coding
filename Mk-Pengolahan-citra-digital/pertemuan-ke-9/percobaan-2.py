# ========================================================
# Praktikum Morfologi Citra - EROSION
# Nama : Satria Alfarizki
# NIM  : 1234567890
# ========================================================

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Path gambar (ubah sesuai lokasi jika perlu)
img_path = r'd:\Satriaalfa\Kuliah\Semester-5\Mk-Pengolahan-citra-digital\pertemuan-ke-9\apex.id-merah.png'

# Membaca gambar dalam mode grayscale
img = cv2.imread(img_path, 0)

# Validasi apakah gambar berhasil dibaca
if img is None:
    print("❌ Gambar tidak ditemukan! Periksa kembali path atau nama file-nya.")
else:
    print("✅ Gambar berhasil dibaca.")
    print("Nama  : Satria Alfarizki")
    print("NIM   : 1234567890")
    print("Proses: EROSION (pengecilan objek)")

    # Membuat elemen struktural 5x5 berbentuk persegi
    kernel = np.ones((5, 5), np.uint8)

    # Melakukan operasi EROSI
    eroded = cv2.erode(img, kernel, iterations=1)

    # Menampilkan hasil
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Gambar Asli')

    plt.subplot(1, 2, 2)
    plt.imshow(eroded, cmap='gray')
    plt.title('Hasil Erosi')

    plt.suptitle('Morfologi Citra - EROSION\nNama: Satria Alfarizki | NIM: 1234567890')
    plt.show()
