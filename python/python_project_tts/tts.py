b= input ("pilih pertanyaan " )
jawaban_kota="jakarta"
j="j"
J='J'
jawaban_daerah ="trenggalek"
t="t"
T="T"
if b == "1":
    nama_kota=input ("ibu kota negara indonesia adalah..." )
    if len(nama_kota)> 7: 
        print('tolol')
    if b=="1" and nama_kota =="jakarta":
        print ("benar")
    for jawab_kota in jawaban_kota :
        if jawab_kota in nama_kota:
            print(jawab_kota,'benar')
    else:
        print('salah')
elif b == "2":
    nama_daerah=input ("kota penghasil tempe kripik di indonesia adalah..." )
    if len(nama_daerah)>10 : 
        print('tolol')
    elif b=="2" and nama_daerah=="trenggalek":
        print ("benar")
    for jawab_daerah in jawaban_daerah :
        if jawab_daerah in nama_daerah:
            print(jawab_daerah,'benar')
    else:
        print('salah')
else:
    print('-')





