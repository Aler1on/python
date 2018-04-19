import texttable as tt

def nilai_mahasiswa():
    nama = []
    nim = []
    nilai_tugas = []
    nilai_uts = []
    nilai_uas = []
    nilai_ahir = []

    i = [[]]

    jawab = "y"

    tab = tt.Texttable()

    while (jawab == "y"):
        print("\n==========================================")
        nama.append (input("\n\tMasukkan Nama Mahasiswa: "))
        nim.append (input("\n\tMasukkan NIM Mahasiswa: "))
        
        tugas = int(input("\n\tNilai Tugas: "))
        tugas = float(tugas)
        nilai_tugas.append(tugas)
        
        uts = int(input("\n\tNilai UTS: "))
        uts = float(uts)
        nilai_uts.append(uts)
        
        uas = int(input("\n\tNilai UAS: "))
        uas = float(uts)
        nilai_uas.append(uas)
        
        hasil = (tugas+uts+uas) /3
        nilai_ahir.append(hasil)
        jawab = input("\n\tTambah Data (y/n)? ")

    for n in nama:
        dxx = nama.index(n)
        i.append([dxx+1,nama[dxx],nim[dxx],nilai_tugas[dxx],nilai_uts[dxx],nilai_uas[dxx],nilai_ahir[dxx]])
    tab.add_rows(i)
    tab.set_cols_align(['l','l','l','r','r','r','r'])
    tab.header (['No','Nama','NIM','Nilai Tugas','Nilai UTS','Nilai UAS','Nilai Ahir'])
    print (tab.draw())

"""    tanya = input("\nKembali ke menu (y/t)?")
    if tanya == "y":
        menu()
    elif tanya == "t":
        exit
    else:
        print ("\n\tMaaf, Keyword yang anda masukkan salah!")"""
