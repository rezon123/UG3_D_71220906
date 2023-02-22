ch = float(input("Masukkan Nilai Curah Hujan : "))
if ch == 0:
  print("Cuaca terang/berawan")
elif ch > 0.5 and ch <= 20:
  print("Curah hujan ringan")
elif ch > 21 and ch <= 50:
  print("Curah hujan sedang")
elif ch > 51 and ch <= 100:
  print("Curah hujan lebat")
else:
  print("Curah hujan ekstrem")