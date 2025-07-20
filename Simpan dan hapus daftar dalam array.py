#mirip sama crud cuma ini ya belum jadi crud , hanya mini aja
# Program untuk mengelola daftar makanan
makanan = ["nasgor", "mie ayam","bakso"]
while True:
    print("\nDaftar makanan saat ini:", makanan)
    print("1. Tambah makanan")
    print("2. Hapus makanan")
    print("3. Tampilkan daftar makanan")
    print("4. Keluar")
    pilihan = input("Pilih menu (1-4): ")
    if pilihan == "1":
        item = input("Masukkan nama makanan yang ingin ditambah: ")
        makanan.append(item)
    elif pilihan == "2":
        item = input("Masukkan nama makanan yang ingin dihapus: ")
        if item in makanan:
            makanan.remove(item)
        else:
            print("Makanan tidak ditemukan.")
    elif pilihan == "3":
        for isi in makanan:
            print(isi)
    elif pilihan == "4":
        break
    else:
        print("Pilihan tidak valid.")