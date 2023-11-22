jumlah=int(input ("masukkan jumlah"))
nama = []
absen= []

for n in range(0, jumlah):
    print (f"data yang dipilih {jumlah}")

    input_nama= input("masukkan nama")
    input_absen= input("masukkan nnomor absen")

    nama.append(input_nama)
    absen.append(input_absen)

for n in range (0,len(nama)):
    data_nama= nama[n]
    data_absen= absen[n]
    print (f"{data_nama} dengan nomor {data_absen} telah absen dikelas")