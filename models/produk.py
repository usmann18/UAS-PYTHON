class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def hitung_total(self, jumlah):
        return self.harga * jumlah
