# Definisikan mapping untuk bobot
bobot_pekerjaan = {
    'ojek': 1,
    'buruh harian lepas': 2,
    'wirausaha': 3,
    'wiraswasta': 4,
    'ojek online': 5,
    'cuci piring': 6,
    'serabutan': 7,
    'karyawan swasta': 8
}

bobot_penghasilan = {
    (0, 500000): 1,
    (500001, 1000000): 2,
    (1000001, float('inf')): 3
}

bobot_kondisi_rumah = {
    'bambu anyam': 1,
    'papan': 2,
    'batu semen': 3,
    'batu permanen': 4
}

bobot_status_rumah = {
    'sewa': 0,
    'milik sendiri': 1
}

bobot_jenis = {
    'miskin extreme': 0,
    'cbp': 1,
    'pkh': 2,
    'tidak layak': 3
}

# Fungsi untuk mengkonversi penghasilan ke bobot
def konversi_penghasilan(penghasilan):
    for range_penghasilan, bobot in bobot_penghasilan.items():
        if range_penghasilan[0] <= penghasilan <= range_penghasilan[1]:
            return bobot
    return 0

def get_bobot_pekerjaan(pekerjaan):
    return bobot_pekerjaan.get(pekerjaan, 0)

def get_bobot_kondisi_rumah(kondisi_rumah):
    return bobot_kondisi_rumah.get(kondisi_rumah, 0)

def get_bobot_status_rumah(status_rumah):
    return bobot_status_rumah.get(status_rumah, 0)