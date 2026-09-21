buah_roh = [
    "Kasih",
    "Sukacita",
    "Damai Sejahtera",
    "Kesabaran",
    "Kemurahan",
    "Kebaikan",
    "Kesetiaan",
    "Kelemahlembutan",
    "Penguasaan Diri"
]

for i in buah_roh:
    print(i)

buah_roh[1] = "Bersukacita"
print(buah_roh)

buah_roh.append("ITULAH KESEMBILAN BUAH - BUAH ROH")
print(buah_roh)

buah_roh.insert(1, "Sukacita")
print(buah_roh)

buah_roh.remove("Bersukacita")
print(buah_roh)

buah_roh.pop(9)
print(buah_roh)

buah_roh.clear()
print(buah_roh)