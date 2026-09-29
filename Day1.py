print("Data Perusahaan")
Prsh=input("Nama Perusahaan:")
Nm=input("Nama:")
jbtn=input("Jabatan:")
print("\n===============================")
print("Nama Perusahaan:",Prsh)
print("Nama:",Nm)
print("Jabatan:",jbtn)
print("\n================================")

print("\nData Medical Check Up")
pt=input("Nama Perusahaan:")
tgl=input("Tanggal Medical Check Up:")
pst=input("Jumlah Peserta:")
print("\n===============================")
print("\nNama Perusahaan:",pt)
print("Tanggal Medical Check Up:",tgl)
print("Jumlah Peserta:",pst)
print("================================")

print("HASIL SAMAPTA PESERTA")

print("\nHasil Lari:")
jarak_lari =1900
if jarak_lari >=2500:
  hasil_lari = "Sangat baik"
elif jarak_lari >=1900:
  hasil_lari = "Baik"
elif jarak_lari >=1400:
  hasil_lari = "Cukup"
else:
  hasil_lari = ("Tidak Lulus")
print(f"{hasil_lari} - {jarak_lari} Meter")

print("\nHasil Berenang:")
jarak_renang=75
if jarak_renang >=90:
  hasil_renang = "Sangat Baik"
elif jarak_renang >=80:
  hasil_renang = "Baik"
elif jarak_renang >=65:
  hasil_renang = "Cukup"
else:
  hasil_renang = "Tidak Lulus"
print(f"{hasil_renang} - {jarak_renang} Meter")

print("\nHasil Pull Up:")
pull_up=18
if pull_up >=20:
  hasil_pull_up = "Sangat Baik"
elif pull_up >=17:
  hasil_pull_up = "Baik"
elif pull_up >=14:
  hasil_pull_up = "Cukup"
else:
  hasil_pull_up = "Tidak Lulus"
print(f"{hasil_pull_up} - {pull_up} Repitisi")
print("\n====RINGKASAN HASIL====")
print(f"Lari: {hasil_lari} ({jarak_lari} Meter)")
print(f"Renang: {hasil_renang} ({jarak_renang} Meter)")
print(f"Pull Up: {hasil_pull_up} ({pull_up} Repitisi)")

print("\n====SELISIH HASIL SAMAPTA====")
print(f"Selisih Lari: {2500 - jarak_lari} Meter Lagi Menuju Nilai Maksimal")
print(f"Selisih Berenang: {100 - jarak_renang} Meter Lagi Menuju Nilai Maksimal")
print(f"Selisih Pull Up: {20 - pull_up} Repitisi Lagi Menuju Nilai Maksimal")