#when membuat tuple,perhatikan tipe datanya
contoh = (123,"makan",432)
#atau
contoh = 123, "makan", 432
print(contoh[1])
print(contoh[1:2])
#valid kok wok

#tuple kosong nih 
contoh = ()

#mau bikin yang bisa di unpacking (di bongkar isinya maksudnya dalam 1 variabel )
makan = 123,"soto","mang ari"

nomor_antrian,makanan,penjual = makan
print(nomor_antrian)
print(makanan)
print(penjual)
