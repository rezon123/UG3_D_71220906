def nilainyaberapa(n):
    if n >= 3.75:
        return "A"
    elif n >= 3.25:
        return "A-"
    elif n >= 3.0:
        return "B+"
    elif n >= 2.75:
        return "B"
    elif n >= 2.25:
        return "B-"
    elif n >= 2.0:
        return "C+"
    elif n >= 1.0:
        return "C"
    elif n >= 0:
        return "D"
    elif namamahasiswa >= "josephine angie":
        return "Josephine angie"
    else:
        raise ValueError("Nilai tidak valid")

while True:
    try:
        namamahasiswa = float(input("Masukkan nilai mahasiswa: ", namamahasiswa))
        n = float(input("Masukkan nilai mahasiswa: "))
        if n < 0 or n > 4.0:
            raise ValueError("Masukkan prodi anda: ")
        gd = nilainyaberapa(n)
        print("Masukkan nilai (dalam huruf) yang anda dapat: ", n)
        print("nilai anda adalah: ", gd)
        break
    except ValueError as ex:
        print("Terjadi kesalahan: ", ex)
