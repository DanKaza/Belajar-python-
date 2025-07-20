# main.py
# Program Belanja Sederhana 
print ("================================")
print ("selamat datang di kaza market")
print ("================================\n")

print ("Berikut adalah daftar barang yang tersedia:")
print ("1. Beras - Rp 10.000")
print ("2. Gula - Rp 8.000")
print ("3. Minyak Goreng - Rp 12.000")
print ("4. Telur - Rp 15.000")
print ("5. Sayur - Rp 5.000")
# Input jumlah masing-masing barang
beras = int(input("Masukkan jumlah Beras yang dibeli: "))
gula = int(input("Masukkan jumlah Gula yang dibeli: "))
minyak = int(input("Masukkan jumlah Minyak Goreng yang dibeli: "))
telur = int(input("Masukkan jumlah Telur yang dibeli: "))
sayur = int(input("Masukkan jumlah Sayur yang dibeli: "))

# Harga satuan
harga_beras = 10000
harga_gula = 8000
harga_minyak = 12000
harga_telur = 15000
harga_sayur = 5000

# Hitung total belanja
total_belanja = (
    beras * harga_beras +
    gula * harga_gula +
    minyak * harga_minyak +
    telur * harga_telur +
    sayur * harga_sayur
)

# Diskon 10% jika total belanja di atas 50.000
if total_belanja > 100000:
    diskon = 0.1 * total_belanja
else:
    diskon = 0

total_setelah_diskon = total_belanja - diskon

print(f"\nTotal belanja: Rp {total_belanja:,}")
print(f"Diskon: Rp {diskon:,}")
print(f"Jumlah yang harus dibayar: Rp {total_setelah_diskon:,}")
print("================================================")
print("Terima kasih telah berbelanja di Kaza Market!")
print("================================================")