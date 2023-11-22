

print("""       


pastikan tidak menggunakan huruf kapital(menggunakan huruf besar)/
                     gunakanlah huruf kecil



kesempatan anda 3x
""")
b= input ("pilih pertanyaan 1-2:...." )
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
e='e'
E='E'
n='n'
N='N'
g='g'
G='G'
l='l'
L='L'
#pertanyaan 1
if b == "1":
    nama_kota=input ("ibu kota negara indonesia adalah..." )
    if len(nama_kota)> 7: 
        print('tolol')
    if b=="1" and nama_kota =="jakarta":
        print ("benar")
    for jawab_kota in jawaban_kota:
        if jawab_kota in nama_kota:
            print(jawab_kota,'benar lainnya salah...')
        else:
            print('JAWABAN SALAH')
    if nama_kota != "jakarta":
        print ("KESEMPATAN ANDA 2X LAGI")
        jawab =input ('silahkan masukkan jawaban lagi....')
        if jawab =='jakarta':
            print ('benar')
        for jawab_kota in jawaban_kota:
            if jawab_kota in jawab:
                print(jawab_kota,'benar lainnya salah...')
        if jawab != 'jakarta':
            print(""" 
            JAWABAN ANDA SALAH COBA 1X LAGI
            """ )
            jawab3= input('jawaban terakhir....')
            if jawab3 != 'jakarta':
                print('kesempatan telah habis')
            if jawab3 != 'jakarta':
                print('silahkan coba lagi')
            else:
                print('benar')
#pertanyaan 1 bagian 2
    if b=="1" and nama_kota=="jakarta":
        nama_daerah=input ("kota penghasil tempe kripik di indonesia adalah..." )
        if len(nama_daerah)>10 : 
            print('tolol')
        if nama_daerah=="trenggalek":
            print ("benar")
        for jawab_daerah in jawaban_daerah :
            if jawab_daerah in nama_daerah:
                print(jawab_daerah, 'benar lainnya salah')
        if nama_daerah != "trenggalek":
            print ("kesempatan anda 2x lagi")
            jawabww =input ('silahkan masukkan jawaban lagi....')
            if jawabww =='trenggalek':
                print ('benar')
            for jawab_daerah in jawaban_daerah :
                if jawab_daerah in jawabww:
                    print(jawab_daerah, 'benar lainnya salah')
            if jawabww != 'trenggalek':
                print(""" 
            JAWABAN ANDA SALAH COBA 1X LAGI
            """ )
                jawabwwww= input('jawaban terakhir....')
                if jawabwwww != 'trenggalek':
                    print('kesempatan telah habis')
                if jawabwwww != 'trenggalek':
                    print('silahkan coba lagi')
                else:
                    print('benar')
        else:
            print('salah')
#pertanyaan 2
elif b == "2":
    nama_daerah=input ("kota penghasil tempe kripik di indonesia adalah..." )
    if len(nama_daerah)>10 : 
        print('tolol')
    if b=="2" and nama_daerah=="trenggalek":
        print ("benar")
    for jawab_daerah in jawaban_daerah :
        if jawab_daerah in nama_daerah:
            print(jawab_daerah, 'benar lainnya salah')
    if nama_daerah != "trenggalek":
        print ("kesempatan anda 2x lagi")
        jawabww =input ('silahkan masukkan jawaban lagi....')
        if jawabww =='trenggalek':
            print ('benar')
        for jawab_daerah in jawaban_daerah :
                if jawab_daerah in jawabww:
                    print(jawab_daerah, 'benar lainnya salah')
        if jawabww != 'trenggalek':
            print(""" 
            JAWABAN ANDA SALAH COBA 1X LAGI
            """ )
            jawabwwww= input('jawaban terakhir....')
            if jawabwwww != 'trenggalek':
                print('kesempatan telah habis')
            if jawabwwww != 'trenggalek':
                print('silahkan coba lagi')
            else:
                print('benar')
    else:
        print('salah')
#pertanyaan 2 bagian 2
    if b=="2" and nama_daerah=="trenggalek":
        nama_kota=input ("ibu kota negara indonesia adalah..." )
    if len(nama_kota)> 7: 
        print('tolol')
    if b=="1" and nama_kota =="jakarta":
        print ("benar")
    for jawab_kota in jawaban_kota :
        if jawab_kota in nama_kota:
            print(jawab_kota,'benar lainnya salah...')
    else:
        print('salah')
    if nama_kota != "jakarta":
        print ("kesempatan anda 2x lagi")
        jawab =input ('silahkan masukkan jawaban lagi....')
        if jawab =='jakarta':
            print ('benar')
        for jawab_kota in jawaban_kota:
            if jawab_kota in jawab:
                print(jawab_kota,'benar lainnya salah...')
        if jawab != 'jakarta':
            print(""" 
            JAWABAN ANDA SALAH COBA 1X LAGI
            """ )
            jawab3= input('jawaban terakhir....')
            if jawab3 != 'jakarta':
                print('kesempatan telah habis')
            if jawab3 != 'jakarta':
                print('silahkan coba lagi')
            else:
                print('benar')
else:
    print('-')
    







