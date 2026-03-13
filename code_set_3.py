"""
Nama File : code_set_3.py
Tujuan Program : Menghitung nilai rata-rata dari sekumpulan data angka
Fitur utama : Menghitung rata-rata dengan membagi jumlah total dengen 
banyak data
Identitas Penulis : Syarifah Febriyani
Tanggal Pembaruan Terakhir : 13 maret 2026

"""
def avg(data):
    """
    Parameter : 
    data : list yang berisi sekumpulan data yang akan dihitung
    rata-ratanya

    Tipe Data :
    integer dan float

    Nilai Kembalian :
    Float (bilangan pecahan)

    Contoh Pemanggilan :
    avg ([5, 10, 15, 20])
    12.5

    """
    total = 0
    for d in data:
        total += d
    return total/len(data)


print(avg([5, 10, 15, 20]))
