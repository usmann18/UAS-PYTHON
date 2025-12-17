import os

# Base directory project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path database SQLite
DB_PATH = os.path.join(BASE_DIR, "database", "data.db")

# Mode aplikasi
DEBUG = True

# App info (opsional, buat laporan)
APP_NAME = "Sistem Manajemen Produk"
APP_VERSION = "1.0"
