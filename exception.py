daftar_nama = []

while True:
    try:
        jumlah = int(input("Berapa jumlah nama yang ingin dimasukan? "))
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0!")
            continue
        break
    except ValueError:
        print("Masukan nilai angka bilangan bulat, bukan string.")

for i in range(jumlah):
    nama = input(f"Nama ke {i+1} : ")
    daftar_nama.append(nama)

print(f"\nDaftar nama: {daftar_nama}")

while True:
    try:
        index = int(input("Panggil nama dengan index ke : "))
        print(f"Nama pada index {index} adalah {daftar_nama[index]}")
        break
    except ValueError:
        print("Masukan nilai angka bilangan bulat, bukan string.")
    except IndexError:
        print("Indek data tersebut tidak tersedia.")