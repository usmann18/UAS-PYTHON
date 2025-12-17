from database.db import get_connection
from models.produk import Produk

class ProdukController:
    def tambah_produk(self, nama, harga):
        conn = get_connection()
        cursor = conn.cursor()

        produk = Produk(nama, harga)

        cursor.execute(
            "INSERT INTO produk (nama, harga) VALUES (?, ?)",
            (produk.nama, produk.harga)
        )

        conn.commit()
        conn.close()
        print("✅ Produk berhasil ditambahkan")

    def tampilkan_produk(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM produk")
        data = cursor.fetchall()

        if not data:
            print("❌ Produk belum ada")
        else:
            for p in data:
                print(f"ID: {p[0]} | Nama: {p[1]} | Harga: Rp{p[2]}")

        conn.close()
