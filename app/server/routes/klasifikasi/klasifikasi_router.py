from flask import Blueprint, render_template, request, redirect
from app.server.routes.klasifikasi import klasifikasi_controller

Klasifikasi = Blueprint('klasifikasi', __name__)

@Klasifikasi.route('/klasifikasi/prediksi', methods=["GET", "POST"])
def validasi():
    if request.method == "GET":
        return render_template("pages/klasifikasi/form.jinja")
    elif request.method == "POST":
        klasifikasi_controller.create()
        return redirect('/klasifikasi/result')
    else:
        return render_template("pages/error/400.jinja")

@Klasifikasi.route('/klasifikasi/result')
def result():
    return render_template("pages/klasifikasi/result.jinja")

@Klasifikasi.route('/klasifikasi/report/training')
def reportnb():
    dataNb = klasifikasi_controller.naiveBayesReport()
    dataDt = klasifikasi_controller.decisionTreeReport()
    print(dataNb)
    print(dataDt)
    print(dataNb["acc"])
    return render_template("pages/klasifikasi/report.jinja", data=dataNb["classReport"])