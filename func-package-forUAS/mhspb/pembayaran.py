def pembayaran():
    print ("\n==================================================")
    nama = input("\n\tMasukkan Nama : ")
    nim = input("\n\tMasukkan NIM : ")
    semester = input("\n\tMasukkan Semester Saat ini : ")
    print("\n\t---Pilihan Pembayaran---")
    print("\t1. Pembayaran SPP")
    print("\t2. Pembayaran UTS")
    print("\t3. Pembayaran UAS")
    print("\t4. Pembayaran SPP dan UTS")
    print("\t5. Pembayaran SPP dan UAS")
    pilih = input("\n\tSilahkan Pilih : ")

    if pilih == "1":
        spp()
    elif pilih == "2":
        uts()
    elif pilih == "3":
        uas()
    elif pilih == "4":
        spp_uts()
    elif pilih == "5":
        spp_uas()
    else:
        exit
        tanya()

def spp():
    bulan = int(input("\n\tJumlah Bulan yang Dibayar: "))
    bulan = float(bulan)
    total = 500000 * bulan
    print ("===========================================================")
    print ("\tTotal bayar SPP Rp. 500000 *" ,bulan," = Rp.",total)

def uts():
    matkul = int(input("\n\tJumlah Mata Kuliah: "))
    matkul = float(matkul)
    byr_uts = 25000 * matkul
    print ("===========================================================")
    print ("\tTotal bayar UTS Rp.25000 *" ,matkul," = Rp.",byr_uts)
    
def uas():
    matkul_uas = int(input("\n\tJumlah Mata Kuliah: "))
    matkul_uas = float(matkul_uas)
    byr_uas = 50000 * matkul_uas
    print ("===========================================================")
    print ("\tTotal bayar UAS Rp. 50000 *" ,matkul," = Rp.",byr_uas)

def spp_uts():
    bulan = int(input("\n\tJumlah Bulan yang Dibayar: "))
    matkul = int(input("\tJumlah Mata Kuliah: "))
    bulan = float(bulan)
    matkul = float(matkul)
    total_spp = 500000 * bulan
    byr_uts = 25000 * matkul
    total = total_spp + byr_uts + 5000
    print ("\n\tTotal Bayar SPP Rp. 500000 * ",bulan," = Rp.",total_spp)
    print ("\tTotal Bayar UTS Rp.25000 * ",matkul," = Rp.",byr_uts)
    print ("\tBiaya tambahan pemeliharaan server sebesar Rp.5000")
    print ("===========================================================")
    print ("\tTotal yang harus dibayar Rp.",total)

def spp_uas():
    bulan = int(input("\n\tJumlah Bulan yang Dibayar: "))
    matkul = int(input("\tJumlah Mata Kuliah: "))
    bulan = float(bulan)
    matkul = float(matkul)
    total_spp = 500000 * bulan
    byr_uas = 50000 * matkul
    total = total_spp + byr_uas + 5000
    print ("\n\tTotal Bayar SPP Rp. 500000 * ",bulan," = Rp.",total_spp)
    print ("\tTotal Bayar UAS Rp.50000 * ",matkul," = Rp.",byr_uas)
    print ("\tBiaya tambahan pemeliharaan server sebesar Rp.5000")
    print ("===========================================================")
    print ("\tTotal yang harus dibayar Rp.",total)
