import os
os.system ("cls")
print("Nama  : Uswatun Khasanah")
print("NIM   : 2209116010")
print("Kelas : SI (A)")
print("")
print("==================================")
print("========= Linear Search ==========")
print("==================================")
print("")

var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

for i in range(len(var)):
    # jika elemen pada indeks i bukan list, tampilkan hasil pencarian
    if type(var[i]) != list:
        print(var[i], "Di Index", i)
    # jika elemen pada indeks i adalah list, cari lagi pada sublist
    else:
        for j in range(len(var[i])):
            print(var[i][j], "Di Index", j, "Pada Kolom", i)
            


