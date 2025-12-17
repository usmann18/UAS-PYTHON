
class Transaksi:
    def __init__(self, user_id, produk_id, jumlah, total):
        self.user_id = user_id
        self.produk_id = produk_id
        self.jumlah = jumlah
        self.total = total

    def detail(self):
        return f"User ID: {self.user_id}, Produk ID: {self.produk_id}, Total: {self.total}"
