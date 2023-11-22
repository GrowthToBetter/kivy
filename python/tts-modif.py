w=3


print("""
                        JAWAB PERTANYAAN DENGAN HURUF KECIL JANGAN GUNAKAN KAPITAL!
        
        kesempatan anda 3x untuk menjawab


"""
)

list_kota=['j','a','k','a','r','t','a']
list_daerah=['t','r','e','n','g','g','a','l','e','k']
b=input("""
            mulai permainan?...(y/n)
""")
if b=='y':
    while True:
        nama_kota= input('masukkan nama ibukota negara indonesia....')
        if nama_kota== 'jakarta' and b=='y':
            print('benar')
            break
        elif nama_kota != 'jakarta':
            w -= 1
            print(f"""
                        KESEMPATAN ANDA BERKURANG 1 KESEMPATAN SAAT INI {w}
            """)
        if nama_kota !='jakarta':
            for kota in list_kota:
                if kota in nama_kota:
                    print(kota,'benar lainnya salah')
        if w==0:
            break
    lanjut= input("""
    ingin lanjut?...(y/n)
    
    """)
    if lanjut=='y':
        while True:
            nama_daerah= input('masukkan nama kota dengan makanan khas tempe kripik sejak dahulu....')
            if nama_daerah== 'trenggalek' and b=='y':
                print('benar')
                break
            elif nama_daerah != 'trenggalek ':
                w -= 1
                print(f"""
                            KESEMPATAN ANDA BERKURANG 1 KESEMPATAN SAAT INI {w}
                """)
            if nama_daerah !='trenggalek':
                for daerah in list_daerah:
                    if daerah in nama_daerah:
                        print(daerah,'benar lainnya salah')
            if w==0:
                break
else:
    print(':)')

        

            
