import texttable as tt
from mhspb.penilaian import nilai_mahasiswa
from mhspb.pembayaran import pembayaran
from mhspb.kalkulator import calc
import getpass

def menu ():
    print("\t========= Created By Andi Purnama =========")
    print("\n\t---Pilihan---")
    print("\t1. Penilaian Mahasiswa")
    print("\t2. Pembayaran Mahasiswa")
    print("\t3. Fungsi Kalkulator")
    print("\t4. Keluar Aplikasi")

    pilih = input("\n\tSilahkan Pilih: ")
    if pilih == "1":
        nilai_mahasiswa()
        tanya()
    elif pilih == "2":
        pembayaran()
        tanya()
    elif pilih == "3":
        calc()
        tanya()
    elif pilih == "4":
        print ("\tTerimakasih")
        exit
    else:
        exit
        tanya()

def tanya():
    tanya = input("\nKembali ke menu (y/t)?")
    if tanya == "y":
        menu()
    elif tanya == "t":
        exit
    else:
        print ("\n\tMaaf, Keyword yang anda masukkan salah!")

username = input("\nUsername : ")
password = getpass.getpass()
print("\t=========================================================")

if username == "21purnama" and password == "21purnama":
    menu()
else:
    print ("Maaf password atau username yang anda masukkan salah!")
