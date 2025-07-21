#mengenal apa itu arg dan kwarg
#ya sama aja baca data tuple atau dictionary
#coba aja liat ini

#ini fungsi args
def kirim_pesan(*no):
    print (no)

#ini fungsi kwargs
def tulis_pesan(**ketik):
    print (ketik)

#manggil fungsi args
kirim_pesan(111,222,333)

#manggil fungsi kwargs
tulis_pesan(tujuan=222, pesan="halo rek")