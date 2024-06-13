from flask import Blueprint, render_template, request, redirect, session
from app.server.routes.klasifikasi import klasifikasi_controller
from app.server.helper import hash


Klasifikasi = Blueprint('klasifikasi', __name__)

@Klasifikasi.route('/klasifikasi/prediksi', methods=["GET", "POST"])
def validasi():
    if 'login' in session:
        if request.method == "GET":
            return render_template("pages/klasifikasi/form.jinja", name=session['name'])
        elif request.method == "POST":
            res = klasifikasi_controller.create()
            if not res:
                return render_template("pages/error/500.jinja", name=session['name'], message="Maaf, server error - gagal menyimpan data")
            nik = request.form.get("nik")
            encrypted_nik = hash.encrypt_nik(nik)
            return redirect(f'/klasifikasi/result/{encrypted_nik}')
        else:
            return render_template("pages/error/400.jinja", name=session['name'])
    else:
        return redirect('/login')

@Klasifikasi.route('/klasifikasi/result/<id>')
def result(id):
    if 'login' in session:
        decrypted_nik = hash.decrypt_nik(id)
        predict = klasifikasi_controller.predict(decrypted_nik)  
        if not predict:
            return render_template("pages/error/500.jinja", name=session['name'], message="Maaf, server error - gagal menyimpan data")
        
        return render_template("pages/klasifikasi/result.jinja", name=session['name'], data=predict)
    else:
        return redirect('/login')

@Klasifikasi.route('/klasifikasi/report/training')
def reportnb():
   if 'login' in session:
        dataNb = klasifikasi_controller.naiveBayesReport()
        dataDt = klasifikasi_controller.decisionTreeReport()
        return render_template("pages/klasifikasi/report.jinja", name=session['name'], nb=dataNb, dt=dataDt)
   else:
       return redirect('/login')