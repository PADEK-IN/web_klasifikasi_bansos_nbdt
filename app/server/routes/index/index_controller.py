from app.server.model.warga import Warga


def count():
    try:
        semua = Warga.query.count()
        miskin_extreme = Warga.query.filter_by(jenis="miskin extreme").count()
        pkh = Warga.query.filter_by(jenis="pkh").count()
        cbp = Warga.query.filter_by(jenis="cbp").count()
        bukan_penerima = Warga.query.filter_by(jenis="tidak layak").count()

        return {
            "semua": semua,
            "miskin_extreme": miskin_extreme,
            "pkh": pkh,
            "cbp": cbp,
            "bukan_penerima": bukan_penerima
        }

    except Exception as e:
        print(e)
        return False
 
 
