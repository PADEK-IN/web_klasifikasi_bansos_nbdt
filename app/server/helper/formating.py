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

def dataUser(data):
    data = {
        "id": data.id,
        "name": data.name,
        "email": data.email
    }
    
    return data

def dataWarga(data):
    data = {
        "nik":data.nik,
        "nama":data.nama,
        "alamat":data.alamat,
        "no_rt":data.no_rt,
        "pekerjaan":data.pekerjaan,
        "penghasilan":data.penghasilan,
        "tanggungan":data.tanggungan,
        "kondisi_rumah":data.kondisi_rumah,
        "status_rumah":data.status_rumah,
        "jenis":data.jenis
        
    }
    
    return data