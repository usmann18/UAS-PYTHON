import sqlite3
import os

DB_NAME = "database/data.db"


def get_connection():
    """
    Membuat koneksi ke database SQLite
    """
    conn = sqlite3.connect(DB_NAME)
    return conn


def create_tables():
    """
    Membuat tabel jika belum ada
    """
    conn = get_connection()
    cursor = conn.cursor()

    # Tabel Users
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)

    # Tabel Produk
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produk (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            harga INTEGER NOT NULL
        )
    """)

    # Tabel Transaksi
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transaksi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            produk_id INTEGER,
            jumlah INTEGER,
            total INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (produk_id) REFERENCES produk(id)
        )
    """)

    conn.commit()
    conn.close()
