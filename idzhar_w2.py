#Data Mahasiswa
print("=== DATA MAHASISWA ===")
nim = input("Masukkan NIM Anda : ")
nama = input("Masukkan Nama Anda : ")
prodi = input("Masukkan Prodi Anda : ")
alamat = input("Masukkan Alamat Anda : ")

#Data UTS & UAS
uts = int(input("Masukkan Nilai UTS Anda : "))
uas = int(input("Masukkan Nilai UAS Anda : "))

#Grade Mahasiswa
nilai = (uts + uas) / 2
if nilai >= 90:
    grade = "A"
elif nilai >= 80:
    grade = "B"
elif nilai >= 70:
    grade = "C"
else:
    grade = "D"

#Hasil Data Mahasiswa
print(f"\n=== DATA DAN NILAI MAHASISWA ===")
print(f"{nim} - {nama} - {prodi} - {alamat}")
# print(f"Nilai UTS : {uts}")
print("Nilai UTS :", uts)
# print(f"Nilai UAS : {uas}")
print("Nilai UAS :", uas)
print(f"Rata-rata Nilai: {(uts + uas) / 2} - {grade}")