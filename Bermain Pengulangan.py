# Bermain Pengulangan
# Program untuk mengulang item belanja
item = ['nasgor','teh','kopi','susu','minyak goreng','beras','gula','telur']
for isi in item:
    print(isi)
# Fungsi untuk mengulang item belanja agar tercetal semua lagi
def ulangi_item():
    while True:
        opsi = input("Apakah ingin mengulang? (y/n): ")
        if opsi.lower() == 'y':
            for isi in item:
                print(isi)
        else:
            print("yaudah")
            break

ulangi_item()