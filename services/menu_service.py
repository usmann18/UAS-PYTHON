from controllers.user_controller import UserController
from controllers.produk_controller import ProdukController
from controllers.transaksi_controller import TransaksiController


class MenuService:
    def __init__(self):
        self.user_controller = UserController()
        self.produk_controller = ProdukController()
        self.transaksi_controller = TransaksiController()

    def tampil_menu(self):
        while True:  # 🔁 PERULANGAN
            print("\n====== MENU UTAMA ======")
            print("1. Tambah User")
            print("2. Lihat User")
            print("3. Tambah Produk")
            print("4. Lihat Produk")
            print("5. Buat Transaksi")
            print("6. Lihat Transaksi")
            print("0. Keluar")

            pilihan = input("Pilih menu: ")

            # 🔀 PERCABANGAN
            if pilihan == "1":
                self.tambah_user()
            elif pilihan == "2":
                self.lihat_user()
            elif pilihan == "3":
                self.tambah_produk()
            elif pilihan == "4":
                self.lihat_produk()
            elif pilihan == "5":
                self.buat_transaksi()
            elif pilihan == "6":
                self.lihat_transaksi()
            elif pilihan == "0":
                print("👋 Terima kasih, program selesai.")
                break
            else:
                print("❌ Pilihan tidak valid!")

    # =======================
    # MENU-MENU DETAIL
    # =======================

    def tambah_user(self):
        nama = input("Nama user  : ")
        email = input("Email user : ")
        self.user_controller.tambah_user(nama, email)

    def lihat_user(self):
        self.user_controller.tampilkan_user()

    def tambah_produk(self):
        nama = input("Nama produk : ")
        harga = int(input("Harga produk: "))
        self.produk_controller.tambah_produk(nama, harga)

    def lihat_produk(self):
        self.produk_controller.tampilkan_produk()

    def buat_transaksi(self):
        user_id = int(input("ID User   : "))
        produk_id = int(input("ID Produk : "))
        jumlah = int(input("Jumlah    : "))
        self.transaksi_controller.buat_transaksi(user_id, produk_id, jumlah)

    def lihat_transaksi(self):
        self.transaksi_controller.tampilkan_transaksi()
