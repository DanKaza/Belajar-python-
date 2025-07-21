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


#nah mari kita coba bikin case nyata nya
def rerata(*nilai):   
    banyak_nlai = len(nilai)
    total = sum(nilai)
    nilai_rerata = float(banyak_nlai) / float(total)
    return nilai_rerata
print(rerata(2,4,1,2,4,1,2,3,4,5,1,8,2))

#nah ini ngitung rerata nilai
