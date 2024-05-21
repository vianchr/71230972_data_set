# input n kategori
n = int(input('Masukkan jumlah kategori: '))
# siapkan dictionary kosong
data_aplikasi = {}
#input nama kategori & aplikasi di dalamnya
for i in range(n):
    nama_kategori = input('Masukkan nama kategori:')
    print('Masukkan 5 nama aplikasi di kategori', nama_kategori)
    
# siapkan list kosong untuk nama-nama aplikasi
    aplikasi = []
    for j in range(5):
        nama_aplikasi = input('Nama aplikasi: ')
        aplikasi.append(nama_aplikasi)
        
# masukkan dalam dictionary
    data_aplikasi[nama_kategori] = aplikasi
    
# tampilkan dictionary data_aplikasi
print(data_aplikasi)

daftar_aplikasi_list = []

# ambil semua daftar aplikasi dari setiap kategori
for aplikasi in data_aplikasi.values():
    daftar_aplikasi_list.append(set(aplikasi))
    
print(f"semua daftar applikasi : {daftar_aplikasi_list}")


# intersection semua kategori
hasil_1 = daftar_aplikasi_list[0]
for i in range(1, len(daftar_aplikasi_list)):
    hasil_1 = hasil_1.intersection(daftar_aplikasi_list[i])
print(f"aplikasi yang muncul di seluruh kategori:  {hasil_1}")

# yang muncul di 1 kategori saja
hasil_2 = daftar_aplikasi_list[0]
for i in range(1, len(daftar_aplikasi_list)):
    hasil_2 = hasil_2.symmetric_difference(daftar_aplikasi_list[i])
    
print(f"aplikasi yang hanya muncul di 1 katgori: {hasil_2-hasil_1}")

#yang muncul tepat di 2 kategori
for i in range(0, len(daftar_aplikasi_list)-1):
    tot=(daftar_aplikasi_list[i]&daftar_aplikasi_list[i+1])-hasil_1
tot=tot|(daftar_aplikasi_list[0]&daftar_aplikasi_list[len(daftar_aplikasi_list)-1])-hasil_1
print (f"aplikasi yang muncul tepat di 2 kategori {tot}")



    