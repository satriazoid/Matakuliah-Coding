import numpy as np
import matplotlib.pyplot as plt
import cv2

nama = "Satria Alfarizki" 
nim = "231011400324"  

image = cv2.imread(r'd:\Satriaalfa\Kuliah\Semester-5\Mk-Pengolahan-citra-digital\pertemuan-ke-10\unpam.png')  

print("="*50)
print(f"PRAKTIKUM EKSTRAKSI CIRI BENTUK")
print(f"Nama: {nama}")
print(f"NIM: {nim}")
print("="*50)

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, binary = cv2.threshold(image_gray, 128, 255, cv2.THRESH_BINARY_INV)

contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if len(contours) == 0:
    print("Tidak ada kontur yang ditemukan!")
    exit()

image_contours = image.copy()
cv2.drawContours(image_contours, contours, -1, (0, 255, 0), 2)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Citra Asli")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(binary, cmap="gray")
plt.title("Citra Biner")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(image_contours, cv2.COLOR_BGR2RGB))
plt.title("Kontur pada Citra")
plt.axis("off")

plt.tight_layout()
plt.show()

shape_features = []

for i, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)
    
    if perimeter > 0:
        circularity = (4 * np.pi * area) / (perimeter ** 2)
    else:
        circularity = 0
    
    moments = cv2.moments(contour)
    
    if moments["m00"] != 0:
        centroid_x = int(moments["m10"] / moments["m00"])
        centroid_y = int(moments["m01"] / moments["m00"])
    else:
        centroid_x = 0
        centroid_y = 0
    
    x, y, w, h = cv2.boundingRect(contour)
    aspect_ratio = w / h if h > 0 else 0
    
    if circularity > 0.9:
        shape_type = "Lingkaran"
    elif circularity > 0.7:
        shape_type = "Mendekati Lingkaran"
    elif circularity > 0.5:
        shape_type = "Oval"
    else:
        shape_type = "Bentuk Lain"
    
    shape_features.append({
        "kontur": i + 1,
        "luas": area,
        "keliling": perimeter,
        "kebulatan": circularity,
        "centroid": (centroid_x, centroid_y),
        "bounding_box": (x, y, w, h),
        "aspect_ratio": aspect_ratio,
        "tipe_bentuk": shape_type
    })

print("\n" + "="*50)
print("HASIL EKSTRAKSI CIRI BENTUK")
print("="*50)

for feature in shape_features:
    print(f"\nKontur {feature['kontur']} - {feature['tipe_bentuk']}:")
    print(f" Luas: {feature['luas']:.2f} piksel")
    print(f" Keliling: {feature['keliling']:.2f} piksel")
    print(f" Kebulatan (circularity): {feature['kebulatan']:.3f}")
    print(f" Centroid: {feature['centroid']}")
    print(f" Bounding Box: {feature['bounding_box']}")
    print(f" Aspect Ratio: {feature['aspect_ratio']:.2f}")

print("\n" + "="*50)
print("STATISTIK KESELURUHAN")
print("="*50)
print(f"Jumlah kontur yang terdeteksi: {len(contours)}")
print(f"Rata-rata kebulatan: {np.mean([f['kebulatan'] for f in shape_features]):.3f}")
print(f"Rata-rata luas: {np.mean([f['luas'] for f in shape_features]):.2f}")

image_with_centroids = image.copy()
for feature in shape_features:
    centroid = feature['centroid']
    cv2.circle(image_with_centroids, centroid, 5, (255, 0, 0), -1) 
    cv2.putText(image_with_centroids, f"{feature['kontur']}", 
                (centroid[0] + 10, centroid[1]), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

plt.figure(figsize=(10, 8))
plt.imshow(cv2.cvtColor(image_with_centroids, cv2.COLOR_BGR2RGB))
plt.title(f"Citra dengan Kontur dan Centroid\nOleh: {nama} ({nim})")
plt.axis("off")
plt.show()