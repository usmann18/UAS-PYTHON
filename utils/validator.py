def valid_email(email):
    """
    Mengecek apakah email valid
    """
    return "@" in email and "." in email


def valid_angka(nilai):
    """
    Mengecek apakah input angka
    """
    return nilai.isdigit()


def input_angka(pesan):
    """
    Input angka dengan validasi
    """
    while True:  # 🔁 PERULANGAN
        nilai = input(pesan)
        if valid_angka(nilai):  # 🔀 PERCABANGAN
            return int(nilai)
        else:
            print("❌ Harus berupa angka!")


def input_email(pesan):
    """
    Input email dengan validasi
    """
    while True:  # 🔁 PERULANGAN
        email = input(pesan)
        if valid_email(email):  # 🔀 PERCABANGAN
            return email
        else:
            print("❌ Format email tidak valid!")
