import pandas as pd
# from flask import request
from app.server import db
from app.server.model.warga import Warga
from app.server.helper import response
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


# def detail(id):
#     try:
#         mhs = Mahasiswa.query.filter_by(id=id).first()
#         if not mhs:
#             return response.badReq([], "Data tidak ditemukan")

#         if not mhs.dosen_satu:
#             dosen1 = None
#         else:
#             dosen_satu = Dosen.query.filter_by(id=mhs.dosen_satu).first()
#             dosen1 = dosen(dosen_satu)

#         if not mhs.dosen_dua:
#             dosen2 = None
#         else:
#             dosen_dua = Dosen.query.filter_by(id=mhs.dosen_dua).first()
#             dosen2 = dosen(dosen_dua)

#         result = detailMhs(mhs, dosen1, dosen2)

#         return result

#     except Exception as e:
#         print(e)
#         return response.serverError()


# def create():
#     try:
#         nim = request.form.get("nim")
#         nama = request.form.get("nama")
#         phone = request.form.get("phone")
#         alamat = request.form.get("alamat")
#         dosen_satu = request.form.get("dosen_satu")
#         dosen_dua = request.form.get("dosen_dua")

#         mhs = Mahasiswa(
#             nim=nim,
#             nama=nama,
#             phone=phone,
#             alamat=alamat,
#             dosen_satu=dosen_satu,
#             dosen_dua=dosen_dua,
#         )

#         db.session.add(mhs)
#         db.session.commit()

#         return response.successCreated("Berhasil menambahkan data mahasiswa")

#     except Exception as e:
#         print(e)
#         return response.serverError()


# def edit(id):
#     try:
#         nim = request.form.get("nim")
#         nama = request.form.get("nama")
#         phone = request.form.get("phone")
#         alamat = request.form.get("alamat")
#         dosen_satu = request.form.get("dosen_satu")
#         dosen_dua = request.form.get("dosen_dua")

#         mhs = Mahasiswa.query.filter_by(id=id).first()

#         mhs.nim = nim
#         mhs.nama = nama
#         mhs.phone = phone
#         mhs.alamat = alamat
#         mhs.dosen_satu = dosen_satu
#         mhs.dosen_dua = dosen_dua

#         db.session.commit()

#         return response.successMsg("Update data berhasil")
#     except Exception as e:
#         print(e)
#         return response.serverError()


# def delete(id):
#     try:
#         mhs = Mahasiswa.query.filter_by(id=id).first()

#         db.session.delete(mhs)
#         db.session.commit()

#         return response.successMsg("Data berhasil dihapus")
#     except Exception as e:
#         print(e)
#         return response.serverError()
