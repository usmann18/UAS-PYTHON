# 📌 Project Python – Sistem Manajemen Produk (SQLite)

## 📖 Deskripsi Proyek

Project ini merupakan aplikasi **Python berbasis CLI (Command Line Interface)** yang dibuat untuk memenuhi tugas/UAS dengan ketentuan:

* Menggunakan **Database SQLite**
* Mengimplementasikan **Modul & Package**
* Menggunakan konsep **OOP (Object Oriented Programming)**
* Mengandung **percabangan (if/elif)** dan **perulangan (while/for)**

Aplikasi ini memungkinkan pengguna untuk:

* Mengelola data **User**
* Mengelola data **Produk**
* Melakukan **Transaksi**

---

## 🛠️ Teknologi yang Digunakan

* **Python 3.x**
* **SQLite3** (database lokal)
* Paradigma **OOP**
* CLI (Terminal)

---

## 📂 Struktur Folder Project

```
python_project/
├── app.py
├── config.py
├── database/
│   ├── __init__.py
│   ├── db.py
│   └── data.db
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── produk.py
│   └── transaksi.py
├── controllers/
│   ├── __init__.py
│   ├── user_controller.py
│   ├── produk_controller.py
│   └── transaksi_controller.py
├── services/
│   ├── __init__.py
│   └── menu_service.py
├── utils/
│   ├── __init__.py
│   └── validator.py
└── README.md
```

---

## 🧠 Penjelasan Folder

### 🔹 `app.py`

Entry point aplikasi. Bertugas:

* Memanggil pembuatan tabel database
* Menjalankan menu utama aplikasi

### 🔹 `config.py`

Menyimpan konfigurasi aplikasi seperti:

* Path database
* Informasi aplikasi

### 🔹 `database/`

Mengelola koneksi database SQLite dan pembuatan tabel.

* `db.py` : koneksi & create table
* `data.db` : file database (data disimpan di sini)

### 🔹 `models/` (OOP)

Berisi class:

* `User`
* `Produk`
* `Transaksi`

Folder ini merupakan implementasi **Object Oriented Programming**.

### 🔹 `controllers/`

Mengatur logika CRUD (Create, Read, Update, Delete) dan penghubung antara model dan database.

### 🔹 `services/`

Berisi menu utama aplikasi yang mengandung:

* Percabangan (`if / elif / else`)
* Perulangan (`while`)

### 🔹 `utils/`

Berisi fungsi bantu (utility), seperti validasi input agar aplikasi lebih aman.

---

## ▶️ Cara Menjalankan Aplikasi

1. Pastikan Python sudah terinstall
2. Buka terminal di folder project
3. Jalankan perintah:

```bash
python app.py
```

4. Menu utama akan tampil di terminal

---

## 📋 Fitur Aplikasi

* ✅ Tambah & lihat user
* ✅ Tambah & lihat produk
* ✅ Buat & lihat transaksi
* ✅ Validasi input
* ✅ Data tersimpan permanen (SQLite)

---

## ✅ Pemenuhan Kriteria Tugas

| Kriteria        | Status |
| --------------- | ------ |
| Database SQLite | ✅      |
| Modul & Package | ✅      |
| OOP             | ✅      |
| Percabangan     | ✅      |
| Perulangan      | ✅      |

---

## 👨‍🎓 Catatan Akademik

Project ini dibuat sebagai **tugas/UAS mata kuliah Pemrograman Python** dan dapat dikembangkan lebih lanjut menjadi aplikasi berbasis web menggunakan Flask atau Django.

---

## ✨ Pengembang

**Nama** : Usman Ramdani
**Program Studi** : Informatika

---

Terima kasih 🙏
