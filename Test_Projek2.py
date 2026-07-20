print("=============== KONVERSI SUHU ===============")

# 1. CELCIUS
def celcius():
    berapa_celcius = int(input("Masukkan suhu dalam derajat celcius : "))

    celcius_ke_reamur = (4 / 5) * berapa_celcius
    celcius_ke_fahrenheit = (9 / 5) * berapa_celcius + 32
    celcius_ke_kelvin = berapa_celcius + 273

    print("CELCIUS KE REAMUR ADALAH :", celcius_ke_reamur, "Derajat R")
    print("CELCIUS KE FAHRENHEIT ADALAH :", celcius_ke_fahrenheit, "Derajat F")
    print("CELCIUS KE KELVIN ADALAH :", celcius_ke_kelvin, "Derajat K")

    print("="*50)

# 2. REAMUR
def reamur():
    berapa_reamur = int(input("Masukkan suhu dalam derajat reamur : "))

    reamur_ke_celcius = (5 / 4) * berapa_reamur
    reamur_ke_fahrenheit = (9 / 4) * berapa_reamur + 32
    reamur_ke_kelvin = (5 / 4) * berapa_reamur + 273

    print("REAMUR KE CELCIUS ADALAH :", reamur_ke_celcius, "Derajat C")
    print("REAMUR KE FAHRENHEIT ADALAH :", reamur_ke_fahrenheit, "Derajat F")
    print("REAMUR KE KELVIN ADALAH :", reamur_ke_kelvin, "Derajat K")

    print("="*50)

# 3. FAHRENHEIT
def fahrenheit():
    berapa_fahrenheit = int(input("Masukkan suhu dalam derajat fahrenheit : "))

    fahrenheit_ke_celcius = (5 / 9) * (berapa_fahrenheit - 32)
    fahrenheit_ke_reamur = (4 / 9) * (berapa_fahrenheit - 32)
    fahreheit_ke_kelvin = 5 / 9 *(berapa_fahrenheit - 32) + 273

    print("FAHRENHEIT KE CELCIUS ADALAH :", fahrenheit_ke_celcius, "Derajat C")
    print("FAHRENHEIT KE REAMUR ADALAH :", fahrenheit_ke_celcius, "Derajat F")
    print("FAHRENHEIT KE KELVIN ADALAH :", fahrenheit_ke_celcius, "Derajat K")

    print("="*50)

# 4. KELVIN
def kelvin():
    berapa_kelvin = int(input("Masukkan suhu dalam derajat kelvin : "))

    kelvin_ke_celcius = berapa_kelvin - 273
    kelvin_ke_reamur = (4 / 5) * (berapa_kelvin - 273)
    kelvin_ke_fahrenheit = (9 / 5) * (berapa_kelvin - 273) + 32

    print("KELVIN KE CELCIUS ADALAH :", kelvin_ke_celcius, "Derajat C")
    print("KELVIN KE REAMUR ADALAH :", kelvin_ke_reamur, "Derajat R")
    print("KELVIN KE FAHRENHEIT ADALAH :", kelvin_ke_fahrenheit, "Derajat F")

repeat = True
while repeat:
    print("1. Menu Celcius")
    print("2. Menu Reamur")
    print("3. Menu Fahrenheit")
    print("4. Menu Kelvin")
    print("5. Menu Exit")

    pilihan = int(input("Pilih Menu : "))

    if pilihan == 1:
        celcius()
    elif pilihan == 2:
        reamur()
    elif pilihan == 3:
        fahrenheit()
    elif pilihan == 4:
        kelvin()
    elif pilihan == 5:
        print("Anda Telah Keluar Dari Program!")
        repeat = False
    else:
        print("Maaf Pilihan Tidak Ada!!")