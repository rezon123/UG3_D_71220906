a = int(input("Masukkan awal deret: ")) #a artinya awal
ak = int(input("Masukkan akhir deret: ")) #ak artinya akhir
d = [str(i) if i % 6 != 0 and i % 8 != 0 else "" for i in range(a, ak)] #d artinya deret
hasilnya = " ".join(d)
print(hasilnya)