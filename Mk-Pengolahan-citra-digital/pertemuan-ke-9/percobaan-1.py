# ========================================================
# Praktikum Morfologi Citra - DILATION
# Nama : Satria Alfarizki
# NIM  : 1234567890
# ========================================================

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Membaca gambar dari file kamu (ubah sesuai nama file)
img = cv2.imread(r'd:\Satriaalfa\Kuliah\Semester-5\Mk-Pengolahan-citra-digital\pertemuan-ke-9\unpam.png', 0)

# Membuat elemen struktural (kernel) berbentuk persegi ukuran 5x5
kernel = np.ones((5, 5), np.uint8)

# Melakukan operasi DILASI
dilated = cv2.dilate(img, kernel, iterations=1)

# Menampilkan hasil
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Gambar Asli')

plt.subplot(1, 2, 2)
plt.imshow(dilated, cmap='gray')
plt.title('Hasil Dilasi')

plt.suptitle('Morfologi Citra - DILASI\nNama: Satria Alfarizki | NIM: 1234567890')
plt.show()
