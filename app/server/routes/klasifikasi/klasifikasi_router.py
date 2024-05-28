from flask import Blueprint, render_template, request, redirect, url_for
from app.server.routes.klasifikasi import klasifikasi_controller

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
        # nik = "1571072411000024"
        dataBaru = klasifikasi_controller.getOne(nik)
        print(dataBaru)
        print(dataBaru["nama"])
        return redirect(url_for('result', data=dataBaru))
    else:
        return render_template("pages/error/400.jinja")

@Klasifikasi.route('/klasifikasi/result')
def result():
    defaultData = {"jenis": "pending"}
    data = request.args.get('data', default=defaultData)
    return render_template("pages/klasifikasi/result.jinja", data=data)

@Klasifikasi.route('/klasifikasi/report/training')
def reportnb():
    dataNb = klasifikasi_controller.naiveBayesReport()
    dataDt = klasifikasi_controller.decisionTreeReport()
    return render_template("pages/klasifikasi/report.jinja", nb=dataNb, dt=dataDt)