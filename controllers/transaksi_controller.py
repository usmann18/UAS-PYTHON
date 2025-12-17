from database.db import get_connection
from models.transaksi import Transaksi

class TransaksiController:
    def buat_transaksi(self, user_id, produk_id, jumlah):
        conn = get_connection()
        cursor = conn.cursor()

        # Ambil harga produk
        cursor.execute("SELECT harga FROM produk WHERE id = ?", (produk_id,))
        produk = cursor.fetchone()

        if produk is None:
            print("❌ Produk tidak ditemukan")
            return

        total = produk[0] * jumlah
        transaksi = Transaksi(user_id, produk_id, jumlah, total)

        cursor.execute("""
            INSERT INTO transaksi (user_id, produk_id, jumlah, total)
            VALUES (?, ?, ?, ?)
        """, (transaksi.user_id, transaksi.produk_id,
              transaksi.jumlah, transaksi.total))

        conn.commit()
        conn.close()
        print("✅ Transaksi berhasil")

    def tampilkan_transaksi(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT t.id, u.nama, p.nama, t.jumlah, t.total
            FROM transaksi t
            JOIN users u ON t.user_id = u.id
            JOIN produk p ON t.produk_id = p.id
        """)

        data = cursor.fetchall()

        if len(data) == 0:
            print("❌ Belum ada transaksi")
        else:
            for t in data:
                print(f"""
ID Transaksi : {t[0]}
User         : {t[1]}
Produk       : {t[2]}
Jumlah       : {t[3]}
Total        : Rp{t[4]}
------------------------
""")

        conn.close()
