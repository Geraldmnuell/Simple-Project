# MEMBUAT PROGRAM KASIR SEDERHANA     
print("\n=============== DAFTAR MENU ===============")
menu_makanan = {
    "Nasi Ayam" : 20000,
    "Nasi Goreng" : 15000,
    "Burger King" : 17000,
    "Roti Bakar" : 10000,
    "Lalapan" : 10000,
    "Gorengan" : 25000,
    "Mie Goreng" : 12000,
    "Mie Bakso" : 15000,
    "Soto Ayam" : 13000,
    "Mie Ayam" : 16000
}

menu_minuman = {
    "Es Teh Manis" : 5000,
    "Teh Hangat" : 5000,
    "Jus Alpukat" : 7000,
    "Es Milo" : 12000,
    "Air Putih" : 4000
}

print("MENU MAKANAN\t\t", "HARGA")
for i in menu_makanan:
    print(i, "\t\t", menu_makanan[i])

print("\nMENU MINUMAN \t\t", "HARGA")
for i in menu_minuman:
    print(i, "\t\t", menu_minuman[i])
print("\nKeterangan : Pesanan dengan jumlah harga \nlebih dari 100.000 akan mendapatkan diskon \nsebesar 15%\n")

print("==================== PILIHAN MENU ====================")
pesan_makan = input("PILIH MENU MAKANAN YANG AKAN DI PESAN : ")
jumlah1 = int(input("JUMLAH MAKANAN YANG AKAN DI PESAN : "))
subtotal1 = jumlah1 * menu_makanan[pesan_makan]

pesan_minum = input("\nPILIH MENU MINUMAN YANG AKAN DI PESAN : ")
jumlah2 = int(input("JUMLAH MINUMAN YANG AKAN DIPESAN : "))
subtotal2 = jumlah2 * menu_minuman[pesan_minum]

subtotal = subtotal1 + subtotal2

if subtotal > 100000:
    diskon = subtotal * (15 / 100)
    total = subtotal - diskon
else:
    total = subtotal

print("\n============================ DETAIL PESANAN ============================")
print("MENU MAKANAN YANG DI PESAN :", pesan_makan, "\tJUMLAH PESANAN :", jumlah1)
print("MENU MINUMAN YANG DI PESAN :", pesan_minum, "\tJUMLAH PESANAN :", jumlah2)
print("TOTAL HARGA PESANAN        : Rp", total)

print("\nTERIMA KASIH SUDAH MEMESAN:)")

