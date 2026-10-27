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
# F3: Cari produk
# ---------------------------------------------------------------
def menu_cari_produk():
    """Mencari produk berdasarkan kode atau nama."""
    print("\n=== Cari Produk ===")
    print("-" * 30)
    print("1. Cari berdasarkan kode")
    print("2. Cari berdasarkan nama")
    print("0. Kembali")

    pilihan = input("Pilih menu (0-2): ").strip()

    if pilihan == "0":
        print("Kembali ke menu utama.")
        return

    if pilihan == "1":
        mode = "kode"
    elif pilihan == "2":
        mode = "nama"
    else:
        print("Pilihan tidak valid. Silakan pilih 0, 1, atau 2.")
        return

    kata_kunci = input(
        f"Masukkan {mode} produk yang dicari: "
    ).strip()

    if not kata_kunci:
        print("Kata kunci pencarian tidak boleh kosong.")
        return

    _, pesan = produk.cari_produk(mode, kata_kunci)

    print("\n" + "=" * 30)
    print("HASIL PENCARIAN".center(30))
    print("=" * 30)
    print(pesan)



# ---------------------------------------------------------------
# F4: Update stok
# ---------------------------------------------------------------
def menu_update_stok():
    """Memperbarui stok produk dengan validasi input."""
    print("\n=== Update Stok Produk ===")
    print("-" * 35)

    kode = input("Kode produk        : ").strip()

    if not kode:
        print("Kode produk tidak boleh kosong.")
        return

    # Periksa apakah produk tersedia
    index = produk.cari_index_by_kode(kode)

    if index == -1:
        print(f"Produk dengan kode '{kode}' tidak ditemukan.")
        return

    # Tampilkan informasi stok saat ini
    data_produk = produk.daftar_produk[index]
    print(f"Nama produk        : {data_produk['nama']}")
    print(f"Stok saat ini      : {data_produk['stok']}")

    stok_baru = input("Masukkan stok baru : ").strip()

    if not stok_baru:
        print("Stok baru tidak boleh kosong.")
        return

    # Kirim perubahan ke fungsi pada produk.py
    berhasil, pesan = produk.update_stok(kode, stok_baru)

    print("\n" + "=" * 35)
    print("HASIL UPDATE STOK".center(35))
    print("=" * 35)
    print(pesan)


# ---------------------------------------------------------------
# F5: Update harga
# ---------------------------------------------------------------
def menu_update_harga():
    """F5: minta kode dan harga baru, kirim ke produk.update_harga."""
    print("\n=== Update Harga Produk ===")
    kode = input("Kode produk  : ")
    harga_baru = input("Harga baru   : ")

    _, pesan = produk.update_harga(kode, harga_baru)
    print(pesan)


# ---------------------------------------------------------------
# F6: Hapus produk
# ---------------------------------------------------------------
def menu_hapus_produk():
    """Meminta konfirmasi sebelum menghapus produk."""

    print("\n=== Hapus Produk ===")
    kode = input("Kode produk yang akan dihapus: ").strip()

    # Validasi kode kosong
    if not kode:
        print("Kode produk tidak boleh kosong.")
        return

    # Periksa apakah produk tersedia
    index = produk.cari_index_by_kode(kode)

    if index == -1:
        print(f"Produk dengan kode '{kode}' tidak ditemukan.")
        return

    # Tampilkan nama produk sebelum konfirmasi
    nama = produk.daftar_produk[index]["nama"]
    print(f"Produk yang akan dihapus: {nama}")

    # Minta konfirmasi pengguna
    konfirmasi = input(
        "Yakin ingin menghapus produk ini? (y/n): "
    ).strip().lower()

    if konfirmasi != "y":
        print("Penghapusan dibatalkan.")
        return

    # Jalankan fungsi penghapusan pada produk.py
    berhasil, pesan = produk.hapus_produk(kode)
    print(pesan)



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
