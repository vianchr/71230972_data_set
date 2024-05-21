def cek_2_file():
    file1 = input("Masukkan nama file pertama: ")
    try:
        with open(file1, 'r') as file:
            isi = file.read()
            isi=isi.lower()
            isi=isi.split(' ')
            kata_kata_1 = (isi)
    except:
        print(f"File '{file1}' tidak ditemukan.")
    
    file2 = input("Masukkan nama file kedua: ")
    try:
        with open(file2, 'r') as file:
            isi = file.read()
            isi=isi.lower()
            isi=isi.split(' ')
            kata_kata_2= (isi)
    except:
        print(f"File '{file1}' tidak ditemukan.")
    
    
    kata_sama = set(kata_kata_1) & set(kata_kata_2)

    if kata_sama:
        print("kata yang muncul pada kedua file:")
        for word in kata_sama:
            print(word)
    else:
        print("Tidak ada kesamaan kata pada kedua file.")

cek_2_file()