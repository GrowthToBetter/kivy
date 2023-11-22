akun={}
key=akun.keys()
pengguna=akun.values()





IsRun=True
while IsRun:
    print("""      SELAMAT DATANG        """)
    acces=input("""SUDAH MEMILIKI ACCOUNT?(y/n)...""")
    if acces=='y':
        input_user=input('masukan username...')
        input_password=input('masukkan password...')
        if input_password in key and input_user in pengguna:
            print('login berhasil')
            break
        else:
            print('tidak ada user')
    elif acces =='n':
        creat=input('buat akun baru(y/n)...')#elif continue jika memilih n
        if creat=='y':
            user=input('masukan user name...')
            while IsRun:
                password=input('masukan password yang terdiri dari 8 huruf...')
                if len(password) <8:
                    print('password kurang!!!')
                    continue
                if len(password) ==8:
                    break
        elif creat=='n':
            continue
    akun.update({password:user})
    print(akun)

            
