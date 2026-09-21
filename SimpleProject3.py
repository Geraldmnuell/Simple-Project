print("========== PROGRAM ATM SEDERHANA ==========")

saldo = 500
cash = 250

while True:
    print("===== MENU PILIHAN =====")
    print("1. MENAMBAHKAN UANG")
    print("2. MENARIK UANG")
    print("3. MENGECEK SALDO")
    print("4. MENGECEK CASH")
    print("5. EXIT MENU")

    operation = int(input("Pilih Menu Yang Sudah Tersedia : "))

    if operation == 1:
        total = float(input("Masukkan total sebagai deposit : "))
        if total > cash:
            print("Kamu tidak mempunyai uang untuk hal ini")
        else:
            saldo = saldo + total
            cash = cash - total
            print(f"Sistem telah berhasil bekerja dan deposit adalah {total}, Jadi saldo kamu sekarang berjumlah {saldo}")
    if operation == 2:
        total = float(input("Masukkan total untuk ditarik : "))
        if total > cash:
            print("Maaf kamu tidak bisa menarik uang")
        else:
            print(f"Selamat kamu berhasil menarik uang, sekarang total ada {total} dan saldo berjumlah {cash}")
    if operation == 3:
        print(f"Saldo kamu sekarang berjumlah : {saldo}")
    if operation == 4:
        print(f"Uang Cash kamu berjumlah : {cash}")
    if operation == 5:
        print("Program ATM Simpel Telah Berjalan Dengan Baik!")
        break
    else:
        print("Menu Tidak Tersedia, Silahkan Coba Lagi")