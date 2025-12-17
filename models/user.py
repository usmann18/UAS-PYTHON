class User:
    def __init__(self, nama, email):
        self.nama = nama
        self.email = email

    def info(self):
        return f"User: {self.nama} | Email: {self.email}"
