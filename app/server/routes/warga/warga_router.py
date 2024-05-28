from flask import Blueprint, request, render_template, redirect
from app.server.routes.warga import warga_controller

Warga = Blueprint('warga', __name__)

@Warga.route("/")
def user():
    if request.method == "GET":
        # mhs = MhsCtrl.allData()
        return render_template("pages/warga/list.jinja")
    else:
        return render_template("pages/error/400.jinja")