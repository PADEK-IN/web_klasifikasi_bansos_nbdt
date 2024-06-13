from hashids import Hashids

# Membuat objek Hashids dengan salt khusus untuk keamanan
hashids = Hashids(salt='my_secret_salt', min_length=16)

def encrypt_nik(nik):
    # Ubah NIK menjadi integer
    nik_int = int(nik)
    # Enkripsi NIK menggunakan Hashids
    encrypted_nik = hashids.encode(nik_int)
    return encrypted_nik

def decrypt_nik(encrypted_nik):
    # Dekripsi NIK menggunakan Hashids
    decoded = hashids.decode(encrypted_nik)
    if decoded:
        return str(decoded[0])
    else:
        return None