import numpy as np

scores = np.array([
    [80, 85, 90],
    [70, 60, 75],
    [95, 90, 100],
    [40, 50, 45]
])

# Rata-rata tiap mahasiswa
rata_rata = np.mean(scores, axis=1)

# Nilai tertinggi
nilai_tertinggi = np.max(scores)

# Status kelulusan
status = np.where(rata_rata >= 70, "Lulus", "Gagal")

print("Rata-rata mahasiswa:", rata_rata)
print("Nilai tertinggi:", nilai_tertinggi)
print("Status kelulusan:", status)