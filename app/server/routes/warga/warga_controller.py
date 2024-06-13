import pandas as pd
from app.server import db
from app.server.model.warga import Warga
from app.server.helper.formating import dataWargaAll


def allData():
    try:
        data = Warga.query.all()
        if not data:
            return "empty"

        return dataWargaAll(data)
    except Exception as e:
        print(e)
        return False
    

def allDataByJenis(jenis):
    try:
        data = Warga.query.filter_by(jenis=jenis)
        if not data:
            return "empty"

        return dataWargaAll(data)
    except Exception as e:
        print(e)
        return False

    
def seeder(file_path):
    try:
        # Membaca data dari file Excel
        data = pd.read_excel(file_path)

        # Iterasi melalui baris-baris di DataFrame
        for index, row in data.iterrows():
            # Konversi penghasilan dari string ke integer
            # penghasilan = int(str(row['penghasilan']).replace('.', ''))

            # Buat instance model dan tambahkan ke sesi
            record = Warga(
                nik=row['nik'],
                nama=row['nama'],
                alamat=row['alamat'],
                no_rt=row['no_rt'],
                pekerjaan=row['pekerjaan'],
                penghasilan=row['penghasilan'],
                tanggungan=row['tanggungan'],
                kondisi_rumah=row['kondisi_rumah'],
                status_rumah=row['status_rumah'],
                jenis=row['jenis']
            )
            db.session.add(record)
            
        # Komit perubahan ke database
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        return False
