#gini le kalau mau bikin fungsi di python
def orang_makan():
    print("Orang makan nasi goreng")
#manggil fungsi
orang_makan()

#nah ini fungsi dengan parameter
def ngomong(ngomong1):
    print(ngomong1)
#manggil fungsi lagi
ngomong("apa coba bjir")

#ini fungsi dengan parameter dan return
def ngitung_luas_balok(panjang, lebar):
    luas = panjang * lebar
    print("piringnya bentuk balok,luasnya : %d" % luas)

ngitung_luas_balok(5, 10)

#======================================================================


#Lanjut variabel global
nama = "wong"
karakter = "jowo"

def tulung_tampilno():
    #kata petani kode ini variabel lokal
    nama = "wong gendeng"
    karakter = "bocah sengklek"
    #buat akses nya wok
    print("nama: %s" % nama)
    print("karakter: %s" % karakter)

    #kalau mau akses variabel global disini
    print("nama: %s" % nama)
    print("karakter: %s" % karakter)

#manggil fungsi tulung_tampilno
tulung_tampilno()