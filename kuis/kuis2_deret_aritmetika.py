# Program Kuis 2 Deret Aritmetika
# Input: suku pertama, beda, dan banyak suku
# Proses: validasi n, membuat deret dengan for,
#         dan menghitung jumlah seluruh suku
# Output: setiap suku dan jumlah deret

print("Deret Aritmetika")

a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))
n = int(input("Banyak suku n: "))

while n <= 0:
    print("n harus bilangan bulat positif.")
    n = int(input("Banyak suku n: "))

total = 0

for i in range(n):
    suku = a + i * d
    total += suku
    print(f"Suku ke-{i + 1}: {suku:.2f}")

print(f"Jumlah = {total:.2f}")