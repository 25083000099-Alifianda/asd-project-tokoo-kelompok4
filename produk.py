"""
produk.py
Modul data produk (Tahap 1: Array of Struct).

Isi file ini:
- F1 tambah_produk   : menambah produk baru (dengan validasi)
- F2 tampilkan_semua_produk : menampilkan semua produk dalam bentuk tabel
- F3 cari_produk      : mencari produk berdasarkan kode (exact) atau nama (partial)
- F4 update_stok      : mengganti stok produk dengan nilai baru

Fitur F3 sampai F6 ditambahkan oleh anggota kelompok lain di bawah bagian F2.
"""

# Array of Struct: seluruh produk disimpan di sini (hilang saat program ditutup)
daftar_produk = []


# ---------------------------------------------------------------
# Fungsi bantu: validasi & format
# ---------------------------------------------------------------
def parse_harga(teks):
    """Ubah teks menjadi float harga. Return (nilai, pesan_error)."""
    try:
        harga = float(teks.strip().replace(",", "."))
    except ValueError:
        return None, "Harga harus berupa angka"

    # float("nan") dan float("inf") lolos float(), jadi dicek manual
    if harga != harga or harga in (float("inf"), float("-inf")):
        return None, "Harga harus berupa angka yang valid"
    if harga <= 0:
        return None, "Harga harus lebih dari 0"
    return harga, None


def parse_stok(teks):
    """Ubah teks menjadi int stok. Return (nilai, pesan_error)."""
    try:
        stok = int(teks.strip())
    except ValueError:
        return None, "Stok harus berupa angka bulat"

    if stok < 0:
        return None, "Stok tidak boleh negatif"
    return stok, None


def format_rupiah(angka):
    """Ubah angka menjadi teks Rupiah, contoh: 15000.0 -> 'Rp 15.000'."""
    if float(angka).is_integer():
        teks = f"{int(angka):,}"
    else:
        teks = f"{angka:,.2f}"
    # Format Python memakai koma sebagai pemisah ribuan, ganti ke gaya Indonesia
    teks = teks.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"Rp {teks}"


# ---------------------------------------------------------------
# Fungsi pencarian internal
# ---------------------------------------------------------------
def cari_index_by_kode(kode):
    """Cari index produk berdasarkan kode (exact match, tidak peka huruf besar/kecil).
    Return index, atau -1 jika tidak ditemukan."""
    kode_bersih = kode.strip().casefold()
    for index, produk in enumerate(daftar_produk):
        if produk["kode_produk"].casefold() == kode_bersih:
            return index
    return -1


# ---------------------------------------------------------------
# F1: Tambah produk
# ---------------------------------------------------------------
def tambah_produk(kode_produk, nama, kategori, harga, stok):
    """Tambah produk baru ke daftar_produk. Return (berhasil, pesan)."""
    kode_produk = kode_produk.strip()
    nama = nama.strip()
    kategori = kategori.strip()

    # Validasi teks: tidak boleh kosong, kode tidak boleh duplikat
    if not kode_produk:
        return False, "Kode produk tidak boleh kosong"
    if cari_index_by_kode(kode_produk) != -1:
        return False, f"Kode produk '{kode_produk}' sudah digunakan"
    if not nama:
        return False, "Nama produk tidak boleh kosong"
    if not kategori:
        return False, "Kategori tidak boleh kosong"

    # Validasi angka: harga > 0 dan stok bilangan bulat >= 0
    harga_valid, error = parse_harga(harga)
    if error:
        return False, error
    stok_valid, error = parse_stok(stok)
    if error:
        return False, error

    # Semua valid, simpan sebagai satu struct (dict)
    daftar_produk.append({
        "kode_produk": kode_produk,
        "nama": nama,
        "kategori": kategori,
        "harga": harga_valid,
        "stok": stok_valid,
    })
    return True, f"Produk {nama} berhasil ditambahkan."


# ---------------------------------------------------------------
# F2: Tampilkan semua produk
# ---------------------------------------------------------------
def buat_tabel_produk(daftar):
    """Susun list produk menjadi teks tabel dengan kolom
    No | Kode | Nama | Kategori | Harga | Stok.
    Dipakai F2 dan bisa dipakai ulang oleh F3 (cari produk)."""
    header = ["No", "Kode", "Nama", "Kategori", "Harga", "Stok"]

    # Siapkan baris data dalam bentuk teks
    baris_data = []
    for nomor, produk in enumerate(daftar, start=1):
        baris_data.append([
            str(nomor),
            produk["kode_produk"],
            produk["nama"],
            produk["kategori"],
            format_rupiah(produk["harga"]),
            str(produk["stok"]),
        ])

    # Lebar tiap kolom = teks terpanjang di kolom tersebut (termasuk header)
    lebar = [len(judul) for judul in header]
    for baris in baris_data:
        for i, isi in enumerate(baris):
            lebar[i] = max(lebar[i], len(isi))

    def format_baris(isi):
        # No, Harga, Stok rata kanan; sisanya rata kiri
        rata_kanan = {0, 4, 5}
        kolom = [
            isi[i].rjust(lebar[i]) if i in rata_kanan else isi[i].ljust(lebar[i])
            for i in range(len(isi))
        ]
        return " | ".join(kolom)

    garis = "-+-".join("-" * panjang for panjang in lebar)
    hasil = [format_baris(header), garis]
    hasil.extend(format_baris(baris) for baris in baris_data)
    return "\n".join(hasil)


def tampilkan_semua_produk():
    """Return string tabel semua produk, atau pesan jika data kosong."""
    if not daftar_produk:
        return "Belum ada produk yang tersimpan."
    return buat_tabel_produk(daftar_produk)


# ---------------------------------------------------------------
# F3: Cari produk
# ---------------------------------------------------------------
def cari_produk(mode, kata_kunci):
    """Cari produk. mode: 'kode' (exact match) atau 'nama' (partial match).
    Return (berhasil, pesan). Jika berhasil, pesan berisi tabel + jumlah hasil."""
    kata_kunci = kata_kunci.strip()
    if not kata_kunci:
        return False, "Kata kunci tidak boleh kosong"

    hasil = []
    if mode == "kode":
        index = cari_index_by_kode(kata_kunci)
        if index != -1:
            hasil.append(daftar_produk[index])
    else:
        kunci = kata_kunci.casefold()
        for item in daftar_produk:
            if kunci in item["nama"].casefold():
                hasil.append(item)

    if not hasil:
        return False, f"Produk dengan {mode} '{kata_kunci}' tidak ditemukan."

    tabel = buat_tabel_produk(hasil)
    return True, f"{tabel}\n\nDitemukan {len(hasil)} produk."


# ---------------------------------------------------------------
# F4: Update stok
# ---------------------------------------------------------------
def update_stok(kode, stok_baru):
    """Ganti stok produk dengan nilai baru (bukan penambahan).
    Return (berhasil, pesan)."""
    kode = kode.strip()
    if not kode:
        return False, "Kode produk tidak boleh kosong"

    index = cari_index_by_kode(kode)
    if index == -1:
        return False, f"Produk dengan kode '{kode}' tidak ditemukan."

    stok_valid, error = parse_stok(stok_baru)
    if error:
        return False, error

    item = daftar_produk[index]
    stok_lama = item["stok"]
    item["stok"] = stok_valid
    return True, (f"Stok produk {item['nama']} berhasil diperbarui: "
                  f"{stok_lama} menjadi {stok_valid}")