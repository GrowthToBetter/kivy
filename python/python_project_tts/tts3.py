print("""       pastikan tidak menggunakan huruf kapital(menggunakan huruf besar)
                                gunakanlah huruf kecil
kesempatan anda 3x
""")
b= input ("pilih pertanyaan " )
jawaban_kota="jakarta"
upper_kota= jawaban_kota.upper()
lower_kota= jawaban_kota.lower()
istitle_kota= jawaban_kota.istitle()
j="j"
J="J"
a='a'
A='A'
k='k'
K='K'
r='r'
R="R"
jawaban_daerah ="trenggalek"
t="t"
T="T"
if b == "1":
    nama_kota=input ("ibu kota negara indonesia adalah..." )
    if len(nama_kota)> 7: 
        print('tolol')
    if b=="1" and nama_kota =="jakarta":
        print ("benar")
    elif status := k in nama_kota and r in nama_kota and t in nama_kota:
        print('k,r,t benar')
    elif status := a in nama_kota and r in nama_kota and t in nama_kota:
        print('a,r,t benar')
    elif status := a in nama_kota and k in nama_kota and t in nama_kota:
        print('k,a,t benar') 
    elif status := a in nama_kota and k in nama_kota and r in nama_kota:
        print('a,k,r benar')
    elif status := j in nama_kota and r in nama_kota and t in nama_kota:
        print('j,r,t benar')
    elif status := j in nama_kota and k in nama_kota and t in nama_kota:
        print ('j,k,t benar')
    elif status := j in nama_kota and k in nama_kota and r in nama_kota:
        print('j,k,r benar')
    elif status := j in nama_kota and a in nama_kota and t in nama_kota:
        print ('j,a,t benar')
    elif status := j in nama_kota and a in nama_kota and r in nama_kota:
        print('j,a,r benar')
    elif status := j in nama_kota and a in nama_kota and k in nama_kota:
        print('j,a,k benar')
    elif status := r in nama_kota and t in nama_kota:
        print ('r,t benar')
    elif status := k in nama_kota and t in nama_kota:
        print ('k,t benar')
    elif status := k in nama_kota and r in nama_kota:
        print('k,r benar')
    elif status := a in nama_kota and t in nama_kota:
        print ('t,a benar')
    elif status := a in nama_kota and r in nama_kota:
        print('a,r benar')
    elif status := a in nama_kota and k in nama_kota:
        print('k,a benar')
    elif status := j in nama_kota and t in nama_kota:
        print ('j,t benar')
    elif status := j in nama_kota and r in nama_kota:
        print('j,r benar')
    elif status := j in nama_kota and k in nama_kota:
        print('j,k benar')
    elif status := j in nama_kota and a in nama_kota:
        print ('j,a benar')
    elif status := t in nama_kota:
        print ('t benar ,lainnya salah')
    elif status := r in nama_kota:
        print ('r benar, lainnya salah')
    elif status := k in nama_kota:
        print ('k benar, lainnya salah')
    elif status := a in nama_kota:
        print ('a benar, lainnya salah')
    elif status  := j in nama_kota:
        print('j benar , lainnya salah')
    else:
        print('salah')
    if nama_kota != "jakarta":
        print ("kesempatan anda 2x lagi")
        jawab =input ('silahkan masukkan jawaban lagi....')
        if jawab =='jakarta':
            print ('benar')
        elif jawab != 'jakarta':
            print(""" 
            JAWABAN ANDA SALAH COBA 1X LAGI
            """ )

       
elif b == "2":
    nama_daerah=input ("kota penghasil tempe kripik di indonesia adalah..." )
    if len(nama_daerah)>10 : 
        print('tolol')
    elif b=="2" and nama_daerah=="trenggalek":
        print ("benar")
    elif status  := t in nama_daerah:
        print('t benar,lainnya salah')
    elif status := T in nama_daerah:
        print('t benar,lainnya salah')
    else:
        print('salah')
else:
    print('-')
    







