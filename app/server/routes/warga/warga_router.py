from flask import Blueprint, request, render_template, redirect
import pandas as pd
from app.server.routes.warga import warga_controller

Warga = Blueprint('warga', __name__)

@Warga.route("/")

def warga():
    df = pd.read_excel('dataset_nonlabel_test.xlsx')
    data = df.to_dict(orient='records')
    return render_template("pages/warga/list.jinja", data=data)
