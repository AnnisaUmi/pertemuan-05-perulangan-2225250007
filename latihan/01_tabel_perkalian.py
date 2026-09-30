# Program tabel perkalian
# Input: satu bilangan bulat
# Proses: mengalikan bilangan dengan 1 sampai 10
# Output: tabel perkalian

n = int(input("Bilangan: "))

for i in range(1, 11):
    hasil = n * i
    print(f"{n} x {i} = {hasil}")