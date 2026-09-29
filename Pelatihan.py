def pesan_menu () :
    # Daftar Pilihan Menu
    menu_makanan = {
        "a" : "Ayam Bakar",
        "b" : "Bebek Bakar",
        "c" : "Ikan Bakar",
    }

    menu_minuman = {
        "a" : "Es Mambo",
        "b" : "Es Cekek",
        "c" : "Es Klepon"
    }

    While True:
        print("Selamat Datang di Restoran Ziyan")

        # 1. Pilih Makanan
        print("\nMenu Makanan:")
        for kode, nama in menu_makanan.items():
            print(f"{kode}. {nama}")

        pilihan_makanan = input("Pilih menu makanan (a/b/c): ").lower()
        while pilihan_makanan not in menu_makanan:
            print("Pilihan tidak tersedia, silahkan pilih kembali.").lower()

        jumlah_makanan = int(input("Pilih Jumlah Makanan:"))

        # 2. Pilih minuman
        print("\nMenu Minuman:")
        for kode, nama in menu_minuman.items():
            print(f"{kode}. {nama}")

        pilihan_makanan = input("Pilih Menu Minuman (a/b/c): ").lower()
        while pilihan_makanan not in menu_minuman:
            print("Pilihan tidak tersedia, silahkan pilih kembali.").lower()

        jumlah_minuman = int(input("Pilih Jumlah Minuman:"))

        # 3. Konfirmasi Pesanan
        print("\nKonfirmasi Pesanan:")
        print(f"Makanan: {menu_makanan[pilihan_makanan]} ({jumlah_makanan} porsi)")
        print(f"Minuman: {menu_minuman[pilihan_makanan]} ({jumlah_minuman} gelas)")"

        konfirmasi = input("Apakah pesanan sudah sesuai? (Ya/Tidak): ").lower()
        if konfirmasi -- "Ya":
            print("\nTerimakasih atas pesanan anda, mohon ditunggu sebentar.")
            break
        else:
            print("\nSilahkan pilih pesanan anda kembali.")

if __name__ == "__main__":
    Pesan Menu()