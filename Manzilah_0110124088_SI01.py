#1. Buat variabel list dengan value : [namakendaraan, jeniskendaraan, cckendaraan, warna kendaraan, roda kendaraan]

kendaraan = ['honda Beat', 'Sepeda Motor', 120, 'Hitam', 2]
print("Kendaraan saya")
print(kendaraan)
print("==========")
# tambahkan dari list tersebut di belakang dengan value : [harga kendaraan, tipe kendaraan]
kendaraan.extend([15000000, "Metic"])
print(kendaraan)
print('=======')
#tambahkan setelah jenis kendaraan dengan valuen[Merk Kendaraan]
kendaraan.insert(2, 'Honda')
print(kendaraan)
print("==========")

# 2. Buat program python dengan match case untuk menghitung luas bangun datar :
# jika pilih 1, maka menghitung luas persegi
# jika pilih 2, maka menghitung luas lingkaran
# jika pilih 3, maka menghitung luas segitiga
# kalau pilihannya tidak ada maka keterangannya : salah pilih

print('Ini adalah program sederhana untuk menghitung luas bangun datar')
print("Pilih Menu angka 1-3 : \n1. Persegi\n2. Lingkaran\n3. Segitiga")
pilihMenu = int(input("Silahkan pilih menu dengan mengetikan angka 1-3: "))

match pilihMenu:
    case 1:
        print("Ini adalah menu untuk menghitung luas persegi")
        sisi = int(input("Masukan nilai yang mau dihitung: "))
        hitung = sisi * sisi
        print (f"Luas persegi adalah : {hitung}")
    case 2:
        print("Ini adalah menu untuk menghitung luas lingkarang") 
        jari_jari = int(input("Masukkan nilai yang mau di hitung: "))
        hitung = 22/7 * jari_jari **2
        print(f"Luas lingkaran adalah : {hitung}")
    case 3:
        print("Ini adalah menu untuk menghitung luas lingkarang")
        alas = int(input("Masukkan alas yang mau di hitung: "))
        tinggi = int(input("Masukkan tinggi yang mau di hitung: "))
        luas = 1/2 * alas * tinggi
        print(f"Luas segitiga adalah : {luas}")
    case _:
        print ("angka tidak valid")