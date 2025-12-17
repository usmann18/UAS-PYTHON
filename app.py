from database.db import create_tables
from services.menu_service import MenuService


def main():
    # 1️⃣ Buat tabel database (jika belum ada)
    create_tables()

    # 2️⃣ Jalankan menu
    menu = MenuService()
    menu.tampil_menu()


if __name__ == "__main__":
    main()
