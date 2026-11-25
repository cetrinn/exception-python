# nama.py - Modul 9 Exception Handling

daftar_nama = []

# 1. Minta jumlah nama, harus angka
while True:
    try:
        jumlah = int(input("Berapa jumlah nama yang akan dimasukan : "))
        break
    except ValueError:
        print("Masukan nilai angka bilangan bulat, bukan string")

# 2. Masukan nama sebanyak jumlah tadi
for i in range(jumlah):
    nama = input(f"Nama ke {i} : ")
    daftar_nama.append(nama)

# 3. Panggil nama berdasarkan index
while True:
    try:
        index = int(input("Panggil nama dengan index ke : "))
        print(f"Nama pada index {index} adalah {daftar_nama[index]}")
        break
    except ValueError:
        print("Masukan nilai angka bilangan bulat, bukan string")
    except IndexError:
        print("Index data tersebut tidak tersedia.")