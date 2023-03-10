import os
os.system ("cls")
print("Nama  : Uswatun Khasanah")
print("NIM   : 2209116010")
print("Kelas : SI (A)")
print("")
print("======================================")
print("========= Sequential Search ==========")
print("======================================")
print("")

var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
i = 0

while i < len(var):
    if type(var[i]) != list:
        print(var[i], "di Index", i)
    else:
        j = 0
        while j < len(var[i]):
            print(var[i][j], "di Index", j, "pada kolom", i)
            j += 1
    i += 1
