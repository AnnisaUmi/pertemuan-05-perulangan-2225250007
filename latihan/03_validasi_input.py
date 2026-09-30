# Program validasi nilai ujian
# Input: nilai antara 0 sampai 100
# Proses: meminta input kembali jika nilai tidak valid
# Output: nilai yang sudah valid

nilai = float(input("Nilai 0-100: "))

while nilai < 0 or nilai > 100:
    print("Nilai tidak valid.")
    nilai = float(input("Nilai 0-100: "))

print(f"Nilai diterima: {nilai}")