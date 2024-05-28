def dataMhs(data):
    array = []

    for i in data:
        array.append(mhs(i))

    return array

def mhs(data):
    data = {
        "id": data.id,
        "nim": data.nim,
        "nama": data.nama,
        "phone": data.phone,
        "alamat": data.alamat,
    }

    return data

def detailMhs(mhs, dosen1, dosen2):
    data = {
        "id": mhs.id,
        "nim": mhs.nim,
        "nama": mhs.nama,
        "phone": mhs.phone,
        "alamat": mhs.alamat,
        "dosen_satu": dosen1,
        "dosen_dua": dosen2,
    }
    return data

def dataUser(data):
    data = {
        "id": data.id,
        "name": data.name,
        "email": data.email
    }
    
    return data