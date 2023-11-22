4#sistem rumus luas keliling dan volume balok
#input user
isrun= True
def input_user():
    panjang= int(input('masukkan panjang balok...'))
    lebar= int(input('masukkan lebar balok...'))
    tinggi= int(input('masukkan tinggi balok...'))
    return panjang,lebar,tinggi 
#rumus volume,luas dan keliling
def keliling_balok(panjang,lebar,tinggi:int)->int: #catatan jangan mencampur adukkan berbagai macam perintah seperti kode keliling dan luas bersamaan
    hasil_keliling=4*(panjang+lebar+tinggi)
    return hasil_keliling
def luas_balok(panjang,lebar,tinggi:int)->int:
    hasil_luas=2*(panjang*lebar*tinggi)
    return hasil_luas
def volume_balok(panjang,lebar,tinggi:int)->int:
    hasil_volume=panjang*lebar*tinggi
    return hasil_volume
while isrun:
    PANJANG,LEBAR,TINGGI=input_user()
    #opsi
    KELILING=keliling_balok(PANJANG,LEBAR,TINGGI)
    LUAS =luas_balok(PANJANG,LEBAR,TINGGI)
    VOLUME=volume_balok(PANJANG,LEBAR,TINGGI)
    opsi=int(input("""
                1.keliling
                2.luas
                3.volume
                4.semuanya
    pilih yang ingin dikonversi....(1/2/3/4)
    """))
    if opsi==1:
        print(f'keliling balok={KELILING}')
    elif opsi==2:
        print(f'luas balok ={LUAS}')
    elif opsi ==3:
        print(f'volume balok={VOLUME}')
    elif opsi==4:
        print(f"balok tersebut memiliki keliling={KELILING},luas ={LUAS},dan volume={VOLUME}")
    else:
        print('pilihan tidak ada pada opsi')
        isrun=False




