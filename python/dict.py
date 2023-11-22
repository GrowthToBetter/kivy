#multi key dictionary
import datetime
import os
import string
import random
mahasiswa1={
    'nama':'asep',
    'nim':'1234',
    'sks_lulus':'120',
    'lahir':datetime.datetime(2004,4,10)
}
mahasiswa2={
    'nama':'iwan',
    'nim':'178904',
    'sks_lulus':'70',
    'lahir':datetime.datetime(2079,8,29)
}
#nesting dict
data_mahasiswam={
    'key1':mahasiswa1,
    'key2':mahasiswa2
}
for mahasiswan in data_mahasiswam.keys():
    KEY =mahasiswan
    NAMA= data_mahasiswam[KEY]['nama']
    SKS=  data_mahasiswam[KEY]['sks_lulus']
    IM=   data_mahasiswam[KEY]['nim']
    print(KEY,NAMA,IM,SKS)


print('-'*80)
os.system('cls')

mahasiswa_template={
    'nama':'nama',
    'nim':00000000,
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,1,11)
    }
while True:
    data_mahasiswa={}
    print(f'{"selamat datang":^20}')
    print(f'{"data mahasiswa":^20}')
    print('-'*20)
    mahasiswa=dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama']=input('nama anda.....')
    mahasiswa['nim']=input('NIM anda.....')
    mahasiswa['sks_lulus']=input('SKS anda.....')
    TAHUN_LAHIR=int(input('tahun lahir(yyyy):....'))
    BULAN_LAHIR=int(input('bulan lahir(1-12):....'))
    TANGGAL_LAHIR=int(input('tanggal lahir(1-30):....'))
    mahasiswa['lahir']=datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
    KEY=''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})
    for mahasiswa in data_mahasiswa:
        KEY=mahasiswa
        NAMA=data_mahasiswa[KEY]['nama']
        NIM=data_mahasiswa[KEY]['nim']
        SKS=data_mahasiswa[KEY]['sks_lulus']
        LAHIR=data_mahasiswa[KEY]['lahir'].strftime('%x')
    print(KEY,NAMA,NIM,SKS,LAHIR)
    
    jut=input('tambah?(y/n).....')
    if jut=='n':
        break



