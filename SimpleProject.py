def ganjil_genap():
    angka0 = int(input("Masukkan angka 0 : "))

    if angka0 % 2 == 0:
        print(f"{angka0} merupakan bilangan genap")
    else:
        print(f"{angka0} merupakan bilangan ganjil")

def bilangan_prima():
    angka1 = int(input("Masukkan angka 1 : "))

    if angka1 < 2:
        print(f"{angka1} bukan bilangan prima")
    else:
        is_prima = True
        for i in range(2, int(angka1 ** 0.5) + 1):
            if angka1 % i == 0:
                is_prima = False
                break

        if is_prima:
            print(f"{angka1} adalah bilangan prima")
        else:
            print(f"{angka1} tidak bilangan prima")

def palindrome():
    angka2 = input("Masukkan angka 2 : ")

    if angka2 == angka2[::-1]:
        print(f"{angka2} merupakan palindrome")
    else:
        print(f"{angka2} bukan palindrome")


def sempurna():
    angka3 = int(input("Masukkan angka 3 : "))
    jumlah_pembagi = 0

    for i in range(1, angka3):
        if angka3 % i == 0:
            jumlah_pembagi += 1

    if jumlah_pembagi == angka3:
        print(f"{angka3} merupakan angka sempurna")
    else:
        print(f"{angka3} bukan angka sempurna")

ulangi = True
while ulangi:
    print("1. MENU GANJIL/GENAP")
    print("2. MENU BILANGAN PRIMA")
    print("3. MENU PALINDROME")
    print("4. MENU ANGKA SEMPURNA")
    print("5. EXIT")

    pilihan = int(input("PILIH MENU : "))
    if pilihan == 1:
        ganjil_genap()
    elif pilihan == 2:
        bilangan_prima()
    elif pilihan == 3:
        palindrome()
    elif pilihan == 4:
        sempurna()
    elif pilihan == 5:
        print("ANDA TELAH KELUAR DARI PILIHAN MENU!")
        ulangi = False
    else:
        print("MENU YANG DIPILIH TIDAK TERSEDIA, SILAHKAN COBA LAGI!")