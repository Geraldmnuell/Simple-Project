# MENGHITUNG RATA RATA NILAI MAHASISWA
print("============== MENGHITUNG NILAI RATA - RATA MAHASISWA ==============")
nama_mahasiswa = [
    "Alok Kurniawan",
    "Anto Speed",
    "Bahlil MBG",
    "Siti Nur Faisah",
    "Ayu Tinting",
    "Reza Alfeus",
    "Rizky Agustian",
    "Bernard Bear",
    "Cinta Mekar",
    "Dewi Iramadan"
]

print("========== DAFTAR NAMA - NAMA MAHASISWA ==========")
for i in nama_mahasiswa:
    print(i)

print("==================================================")
pilihan_mahasiswa = int(input("\nPilih Mahasiswa : "))
total_penilaian = 3

""""
PROGRAM MENGHITUNG NILAI RATA - RATA MAHASISWA YANG ADA PADA DAFTAR
"""
if pilihan_mahasiswa >= 1 and pilihan_mahasiswa <= len(nama_mahasiswa):
    nama = nama_mahasiswa[pilihan_mahasiswa - 1]

    print(f"Masukkan Nilai Mahasiswa {nama}")
    nilai_tugas = float(input("Nilai Tugas : "))
    nilai_uts = float(input("Nilai UTS : "))
    nilai_uas = float(input("Nilai UAS : "))

    process_sum = nilai_tugas + nilai_uts + nilai_uas
    average = process_sum / total_penilaian
    print("\n========== RESULT MAHASISWA ===========")

    print(f"Nama Mahasiswa       : {nama}")
    print(f"Nilai Tugas          : {nilai_tugas}")
    print(f"Nilai UTS            : {nilai_uts}")
    print(f"Nilai UAS            : {nilai_uas}")
    print("=======================================")
    print(f"Rata - Rata Nilai    : {average:.2f}")

    if average >= 60:
        print("Status               : LULUS")
    else:
        print("Status               : TIDAK LULUS")
else:
    print("Pilihan Mahsiswa Tidak Tersedia, COBA LAGI!!")

