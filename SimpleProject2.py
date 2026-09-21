# KONVERSI DOLAR KE RUPIAH
dolar = float(input("KONVERSI BERAPA DOLAR : $")) # ONLY INPUT 1 - 99 DOLAR
dolar_per_rupiah = 16.000

dolar_ke_rupiah = dolar * dolar_per_rupiah
print(f"TOTALNYA SEBESAR : Rp{dolar_ke_rupiah:.3f}")

# KONVERSI RUPIAH KE DOLAR
rupiah = float(input("KONVERSI BERAPA RUPIAH : Rp"))
rupiah_per_dolar = 16.000

rupiah_ke_dolar = rupiah / rupiah_per_dolar
print(f"TOTALNYA SEBESAR : ${rupiah_ke_dolar:.1f} USD")