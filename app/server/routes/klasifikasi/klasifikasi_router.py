from flask import Blueprint, render_template, request, redirect
from app.server.routes.klasifikasi import klasifikasi_controller
from app.server.helper import hash


Klasifikasi = Blueprint('klasifikasi', __name__)

@Klasifikasi.route('/klasifikasi/prediksi', methods=["GET", "POST"])
def validasi():
    if request.method == "GET":
        return render_template("pages/klasifikasi/form.jinja")
    elif request.method == "POST":
        res = klasifikasi_controller.create()
        if not res:
            return render_template("pages/error/500.jinja", message="Maaf, server error - gagal menyimpan data")
        nik = request.form.get("nik")
        encrypted_nik = hash.encrypt_nik(nik)
        return redirect(f'/klasifikasi/result/{encrypted_nik}')
    else:
        return render_template("pages/error/400.jinja")

@Klasifikasi.route('/klasifikasi/result/<id>')
def result(id):
    decrypted_nik = hash.decrypt_nik(id)
    predict = klasifikasi_controller.predict(decrypted_nik)  
    if not predict:
        return render_template("pages/error/500.jinja", message="Maaf, server error - gagal menyimpan data")
    
    return render_template("pages/klasifikasi/result.jinja", data=predict)

@Klasifikasi.route('/klasifikasi/report/training')
def reportnb():
    dataNb = klasifikasi_controller.naiveBayesReport()
    dataDt = klasifikasi_controller.decisionTreeReport()
    return render_template("pages/klasifikasi/report.jinja", nb=dataNb, dt=dataDt)