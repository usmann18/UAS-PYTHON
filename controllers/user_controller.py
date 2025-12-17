from database.db import get_connection
from models.user import User

class UserController:
    def tambah_user(self, nama, email):
        conn = get_connection()
        cursor = conn.cursor()

        user = User(nama, email)

        cursor.execute(
            "INSERT INTO users (nama, email) VALUES (?, ?)",
            (user.nama, user.email)
        )

        conn.commit()
        conn.close()
        print("✅ User berhasil ditambahkan")

    def tampilkan_user(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()

        if len(users) == 0:
            print("❌ Data user kosong")
        else:
            for user in users:
                print(f"ID: {user[0]} | Nama: {user[1]} | Email: {user[2]}")

        conn.close()
