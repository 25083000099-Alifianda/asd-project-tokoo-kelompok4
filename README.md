# Sistem Manajemen Toko / Inventori

Program berbasis **Command Line Interface (CLI)** untuk mengelola data produk toko, dibangun dengan Python menggunakan struktur data **Array of Struct** (list of dict).

> **Project Algoritma dan Struktur Data — Checkpoint UTS Tahap 1**
> Sistem Informasi, FTI Universitas Merdeka Malang · Semester 3 · Tahun Ajaran 2026/2027
> Dosen Pengampu: Amadea Permana

---

## Kelompok 4

| No | Nama Lengkap | NIM |
| --- | --- | --- |
| 1 | Livia Agistina Afrizal | 25083000077 |
| 2 | Karuniansyah Daryawan P. L. | 25083000083 |
| 3 | Muhammad Irsyad Firmansyah | 25083000094 |
| 4 | Alifianda Nur Mahardika | 25083000099 |

---

## Deskripsi Sistem

Sistem ini membantu operator toko (pemilik atau admin) mencatat dan mengelola data produk tanpa pencatatan manual di buku. Data produk disimpan di memori sebagai list yang berisi dictionary, dengan lima atribut untuk setiap produk:

| Atribut | Tipe | Contoh | Aturan |
| --- | --- | --- | --- |
| `kode_produk` | `str` | `"PRD001"` | Unik, tidak boleh kosong, pengecekan tidak membedakan huruf besar/kecil |
| `nama` | `str` | `"Minyak Goreng 1L"` | Tidak boleh kosong |
| `kategori` | `str` | `"Sembako"` | Tidak boleh kosong |
| `harga` | `float` | `15000.0` | Angka lebih dari 0 |
| `stok` | `int` | `50` | Bilangan bulat, tidak negatif |

> **Catatan:** pada Tahap 1 data hanya berada di memori dan akan hilang saat program ditutup, sesuai ketentuan brief.

---

## Cara Menjalankan

**Prasyarat:** Python 3 terpasang. Tidak memerlukan library eksternal.

```bash
# 1. Clone repository
git clone https://github.com/[username]/asd-project-toko-kelompok4.git

# 2. Masuk ke folder project
cd asd-project-toko-kelompok4

# 3. Jalankan program
python main.py
```

Setelah program berjalan, pilih menu dengan mengetik angka lalu tekan Enter. Setelah satu fitur selesai, program kembali ke menu utama sampai memilih `0` (Keluar).

```text
========================================
               MENU UTAMA
========================================
1. Tambah Produk Baru
2. Tampilkan Semua Produk
3. Cari Produk
4. Update Stok Produk
5. Update Harga Produk
6. Hapus Produk
0. Keluar
----------------------------------------
Pilih menu (0-6):
```

---

## Daftar Fitur

| Kode | Fitur | Fungsi | Keterangan |
| --- | --- | --- | --- |
| F1 | Tambah Produk Baru | `tambah_produk()` | Validasi kode (tidak kosong, tidak duplikat), nama, kategori, harga, dan stok |
| F2 | Tampilkan Semua Produk | `tampilkan_semua_produk()` | Tabel dengan kolom No, Kode, Nama, Kategori, Harga, Stok; lebar kolom menyesuaikan isi |
| F3 | Cari Produk | `cari_produk()` | Berdasarkan kode (exact match) atau nama (partial match, tidak peka huruf besar/kecil) |
| F4 | Update Stok | `update_stok()` | Menampilkan stok sebelumnya dan stok sekarang |
| F5 | Update Harga | `update_harga()` | Menampilkan harga lama dan harga baru dalam format Rupiah |
| F6 | Hapus Produk | `hapus_produk()` | Menghapus produk berdasarkan kode, dengan langkah konfirmasi (y/n) |

### Validasi Input

- Kode produk tidak boleh kosong dan tidak boleh duplikat (tidak membedakan huruf besar/kecil).
- Nama dan kategori tidak boleh kosong.
- Harga harus berupa angka dan lebih dari 0 (koma desimal diterima; `nan` dan `inf` ditolak).
- Stok harus bilangan bulat dan tidak negatif (nilai desimal seperti `1.5` ditolak).
- Kode produk pada fitur cari, update, dan hapus harus ada di sistem.

---

## Struktur Folder

```text
asd-project-toko-kelompok4/
|-- main.py      # Entry point dan menu utama
|-- produk.py    # Data produk (Array of Struct) dan fungsi 6 fitur
`-- README.md    # Dokumentasi proyek
```

- **`main.py`** — titik masuk program; menjalankan perulangan menu, membaca input operator, dan memanggil fungsi fitur.
- **`produk.py`** — berisi list `daftar_produk`, fungsi bantu (`parse_harga`, `parse_stok`, `format_rupiah`, `cari_index_by_kode`, `buat_tabel_produk`), dan enam fungsi fitur. Fungsi di file ini menerima parameter dan mengembalikan `(berhasil, pesan)` atau teks tabel.

---

## Pembagian Tugas

| Anggota | Bagian yang Dikerjakan | File / Fungsi |
| --- | --- | --- |
| **Muhammad Irsyad Firmansyah** | F1 Tambah Produk beserta seluruh validasi input dan F2 Tampilkan Semua Produk | `produk.py`: `tambah_produk()`, `parse_harga()`, `parse_stok()`, `tampilkan_semua_produk()`, `buat_tabel_produk()` |
| **Alifianda Nur Mahardika** | F3 Cari Produk dan F4 Update Stok serta, README | `produk.py`: `cari_produk()`, `cari_index_by_kode()`, `format_rupiah()`, `update_stok()`, `README.md`|
| **Livia Agistina Afrizal** | F5 Update Harga dan penyusunan laporan | `produk.py`: `update_harga()` |
| **Karuniansyah Daryawan P. L.** | F6 Hapus Produk, menu utama | `produk.py`: `hapus_produk()` · `main.py`: `tampilkan_menu()`, `main()` · |

---

## Rencana Pengembangan

| Tahap | Pengembangan |
| --- | --- |
| 2 | Riwayat transaksi dengan Linked List |
| 3 | Fitur undo dengan Stack |
| 4 | Antrian checkout dengan Queue dan kategori produk dengan Tree |
| 5 | Sorting data produk dan laporan |

---

<sub>Algoritma dan Struktur Data · Sistem Informasi — FTI Unmer Malang · 2026/2027</sub>
