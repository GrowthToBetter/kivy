buku=[]
while True:
    judul= input('masukkan judul buku...')
    penerbit= input('masukkan penerbit buku...')
    buku_1=[judul,penerbit]
    buku.append(buku_1)
    for h,n in enumerate(buku):
        print(h+1,n[0],n[1])
    lanjjut= input('ada lagi?...y/n')
    if lanjjut=='n':
        break
