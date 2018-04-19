def tambah() :
    print ("\tBerikut adalah fungsi PENJUMLAHAN")
    a = int(input("\n\tSilahkan masukkan nilai x = "))
    b = int(input("\tSilahkan masukkan nilai y = "))
    c = a + b
    print ("\t x + y = ",c)
    tanya()

def kurang() :
    print ("\tBerikut adalah fungsi PENGURANGAN")
    a = int(input("\n\tSilahkan masukkan nilai x = "))
    b = int(input("\tSilahkan masukkan nilai y = "))
    c = a - b
    print ("\t x - y = ",c)
    tanya()

def bagi() :
    print ("\tBerikut adalah fungsi PEMBAGIAN")
    a = int(input("\n\tSilahkan masukkan nilai x = "))
    b = int(input("\tSilahkan masukkan nilai y = "))
    c = a / b
    print ("\t x : y = ",c)
    tanya()

def kali() :
    print ("\tBerikut adalah fungsi PERKALIAN")
    a = int(input("\n\tSilahkan masukkan nilai x = "))
    b = int(input("\tSilahkan masukkan nilai y = "))
    c = a * b
    print ("\t x * y = ",c)
    tanya()

def tanya() :
    tanya = input("\t\nKembali ke menu kalkulator (y/t)?")
    if tanya == "y":
        calc()
    elif tanya == "t":
        exit
    else:
        print ("\n\tMaaf, Keyword yang anda masukkan salah")

def calc() :
    print ("\t=====================================================")
    print ("\tProgram Kalkulator Sederhana")
    print ("\t=====================================================")
    print ("\t1. Penjumlahan")
    print ("\t2. Pengurangan")
    print ("\t3. Pembagian")
    print ("\t4. Perkalian")
    print ("\t=====================================================")
    print ("\tSilahkan Pilih Fungsi yang akan anda gunakan (1-4)")
    pil = input("\n\tMasukkan Pilihan: ")
    if pil == "1":
        tambah()
    elif pil == "2":
        kurang()
    elif pil == "3":
        bagi()
    elif pil == "4":
        kali()
    else:
        print ("\nMaaf, keyword yang anda masukkan salah")
        print ("\nCoba ulangi kembali")
        tanya()
