temperatures = [25, 28, 30, 22, 35, 40, 18, 24]

# Konversi Celsius ke Fahrenheit
temp_fahrenheit = [(c * 9/5) + 32 for c in temperatures]

# Mengambil 3 data terakhir
last_three = temp_fahrenheit[-3:]

print("Suhu Fahrenheit:", temp_fahrenheit)
print("3 suhu terakhir:", last_three)