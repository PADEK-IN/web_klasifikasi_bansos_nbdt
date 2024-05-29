import os
from flask import Blueprint, request, render_template, redirect
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

@Warga.route("/seeder")
def seeder():
    # Menentukan path file Excel relatif terhadap root project
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../../dataset.xlsx')
    seed = warga_controller.seeder(file_path)
    if not seed:
        return render_template("pages/error/500.jinja", name="Admin")
    
    return redirect("/warga")
