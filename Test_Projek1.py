# MEDIUM TRY
print("========== DISPLAY OF CALCULATOR ==========\n")
input1 = int(input("Masukkan angka pertama : "))
input2 = int(input("Masukkan angka kedua : "))

ulangi = True
while ulangi:
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Modulus")
    print("6. Exit")

    pilihan = int(input("Masukkan menu : "))

    if pilihan == 1:
        penjumlahan = input1 + input2
        print("Hasil Penjumlahan :", penjumlahan)
    elif pilihan == 2:
        pengurangan = input1 - input2
        print("Hasil Pengurangan :", pengurangan)
    elif pilihan == 3:
        perkalian = input1 * input2
        print("Hasil Perkalian :", perkalian)
    elif pilihan == 4:
        if input2 == 0:
            print("Pembagi 0 tidak diperbolehkan!!!") # MENANGANI CASE YANG INPUT PEMBAGI ADALAH NOL(0)
        else:
            pembagian = input1 / input2
            print("Hasil Pembagian :", pembagian)
    elif pilihan == 5:
        modulus = input1 % input2
        print("Hasil Modulus :", modulus)
    elif pilihan == 6:
        print("Program Selesai")
        ulangi = False
    else:
        print("Pilihan tidak valid, coba kembali!")