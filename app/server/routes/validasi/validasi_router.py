from flask import Blueprint, render_template, request, redirect
from app.server.routes.validasi import validasi_controller

Validasi = Blueprint('validasi', __name__)

@Validasi.route('/validasi', methods=["GET", "POST"])
def validasi():
    if request.method == "GET":
        return render_template("pages/validasi/form.jinja")
    elif request.method == "POST":
        validasi_controller.create()
        return redirect('/validasi/result')
    else:
        return render_template("pages/error/400.jinja")

@Validasi.route('/validasi/result')
def result():
    return render_template("pages/validasi/result.jinja")

@Validasi.route('/report/training')
def reportnb():
    dataNb = validasi_controller.naiveBayesReport()
    dataDt = validasi_controller.decisionTreeReport()
    print(dataNb)
    print(dataDt)
    print(dataNb["acc"])
    return render_template("pages/validasi/report_nb.jinja")