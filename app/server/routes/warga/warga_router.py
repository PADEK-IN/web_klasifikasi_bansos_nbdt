import os
from flask import Blueprint, render_template, redirect
# import pandas as pd
from app.server.routes.warga import warga_controller

Warga = Blueprint('warga', __name__)

@Warga.route("/")
def warga():
    # df = pd.read_excel('dataset_nonlabel_test.xlsx')
    # data = df.to_dict(orient='records')
    
    result = warga_controller.allData()
    if not result:
        return render_template("pages/error/500.jinja", name="Admin")
    return render_template("pages/warga/list.jinja", name="Admin", data=result)

@Warga.route("/miskin-extreme")
def miskinextreme():
    result = warga_controller.allDataByJenis("miskin extreme")
    if not result:
        return render_template("pages/error/500.jinja", name="Admin")
    return render_template("pages/warga/miskin_extreme.jinja", name="Admin", data=result)

@Warga.route("/pkh")
def pkh():
    result = warga_controller.allDataByJenis("pkh")
    if not result:
        return render_template("pages/error/500.jinja", name="Admin")
    return render_template("pages/warga/pkh.jinja", name="Admin", data=result)

@Warga.route("/cbp")
def cbp():
    result = warga_controller.allDataByJenis("cbp")
    if not result:
        return render_template("pages/error/500.jinja", name="Admin")
    return render_template("pages/warga/cbp.jinja", name="Admin", data=result)

@Warga.route("/bukan-penerima")
def bukan_penerima():
    result = warga_controller.allDataByJenis("tidak layak")
    if not result:
        return render_template("pages/error/500.jinja", name="Admin")
    return render_template("pages/warga/bukan_penerima.jinja", name="Admin", data=result)

@Warga.route("/seeder")
def seeder():
    # Menentukan path file Excel relatif terhadap root project
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../../dataset.xlsx')
    seed = warga_controller.seeder(file_path)
    if not seed:
        return render_template("pages/error/500.jinja", name="Admin")
    
    return redirect("/warga")
