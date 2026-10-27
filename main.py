import produk

LEBAR_GARIS = 44


# ---------------------------------------------------------------
# Tampilan umum
# ---------------------------------------------------------------
def tampilkan_header():
    """Tampilkan judul program."""
    print("=" * LEBAR_GARIS)
    print("SISTEM MANAJEMEN TOKO / INVENTORI".center(LEBAR_GARIS))
    print("=" * LEBAR_GARIS)


def tampilkan_menu_utama():
    """Tampilkan daftar menu utama."""
    print("\n" + "-" * LEBAR_GARIS)
    print("MENU UTAMA".center(LEBAR_GARIS))
    print("-" * LEBAR_GARIS)
    print("1. Tambah Produk Baru")
    print("2. Tampilkan Semua Produk")
    print("3. Cari Produk")
    print("4. Update Stok Produk")
    print("5. Update Harga Produk")
    print("6. Hapus Produk")
    print("0. Keluar")
    print("-" * LEBAR_GARIS)


def tunggu_enter():
    """Beri jeda agar operator sempat membaca hasil sebelum menu muncul lagi."""
    input("\nTekan Enter untuk kembali ke menu...")


# ---------------------------------------------------------------
# F1: Tambah produk
# ---------------------------------------------------------------
def menu_tambah_produk():
    """Minta data produk dari operator lalu kirim ke produk.tambah_produk."""
    print("\n=== Tambah Produk Baru ===")
    kode = input("Kode produk : ")
    nama = input("Nama        : ")
    kategori = input("Kategori    : ")
    harga = input("Harga (Rp)  : ")
    stok = input("Stok        : ")

    _, pesan = produk.tambah_produk(kode, nama, kategori, harga, stok)
    print(pesan)


# ---------------------------------------------------------------
# F2: Tampilkan semua produk
# ---------------------------------------------------------------
def menu_tampilkan_semua():
    """Tampilkan tabel semua produk."""
    print("\n=== Daftar Semua Produk ===")
    print(produk.tampilkan_semua_produk())


# ---------------------------------------------------------------
# Iki fitur 3-6 diganti/di isi sesuai fiturmu,mbok delete moro mbok copas tekmu yo rapopo 
# ---------------------------------------------------------------
def menu_cari_produk():
    # TODO (anggota lain): F3 Cari Produk
    print("\nFitur Cari Produk belum tersedia.")


def menu_update_stok():
    # TODO (anggota lain): F4 Update Stok
    print("\nFitur Update Stok belum tersedia.")


def menu_update_harga():
    # TODO (anggota lain): F5 Update Harga
    print("\nFitur Update Harga belum tersedia.")


def menu_hapus_produk():
    # TODO (anggota lain): F6 Hapus Produk
    print("\nFitur Hapus Produk belum tersedia.")


# ---------------------------------------------------------------
# Program utama
# ---------------------------------------------------------------
# Pemetaan pilihan menu ke fungsi yang dijalankan
AKSI_MENU = {
    "1": menu_tambah_produk,
    "2": menu_tampilkan_semua,
    "3": menu_cari_produk,
    "4": menu_update_stok,
    "5": menu_update_harga,
    "6": menu_hapus_produk,
}


def main():
    """Loop utama: tampilkan menu, baca pilihan, jalankan fitur."""
    tampilkan_header()

    while True:
        tampilkan_menu_utama()
        pilihan = input("Pilih menu (0-6): ").strip()

        if pilihan == "0":
            print("\nTerima kasih. Program selesai.")
            break

        aksi = AKSI_MENU.get(pilihan)
        if aksi is None:
            print("Pilihan tidak valid. Masukkan angka 0 sampai 6.")
            continue

        aksi()
        tunggu_enter()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C / Ctrl+D: keluar dengan rapi, tanpa pesan error panjang
        print("\n\nProgram dihentikan.")
