from flask import Blueprint, request, render_template, redirect
from app.server.routes.warga import warga_controller

Warga = Blueprint('warga', __name__)

@Warga.route("/", methods=["GET", "POST"])
def user():
    if request.method == "GET":
        # mhs = MhsCtrl.allData()
        return render_template("pages/warga/list.html")
    elif request.method == "POST":
        # MhsCtrl.create()
        return redirect('/warga')
    else:
        return render_template("pages/error/400.html")
    
# @Warga.route("/user/add", methods=["GET"])
# def addMahasiswa():
#     if request.method == "GET":
#         # nameType = [
#         #     {"type": "text", "name": "nim", "text": "NIM"},
#         #     {"type": "text", "name": "nama", "text": "Nama"},
#         #     {"type": "text", "name": "phone", "text": "No Telepon"},
#         #     {"type": "text", "name": "alamat", "text": "Alamat"},
#         # ]
#         # dosens = DosenCtrl.allData()
#         return render_template("pages/user/add.html")
#     else:
#         return render_template("pages/error/400.html")
    
# @Warga.route("/user/<id>", methods=["GET"])
# def detailMhs(id):
#     # MhsCtrl.detail(id)
#     return render_template("pages/user/detail.html")
    
# @Warga.route("/user/edit/<id>", methods=["GET", "POST"])
# def editMhs(id):
#     if request.method == "GET":
#         return "Form Edit Data"
#     elif request.method == "POST":
#         return MhsCtrl.edit(id)
#     else:
#         return render_template("pages/error/400.html")
    
# @Warga.route("/user/delete/<id>", methods=["GET"])
# def deleteMhs(id):
#     return MhsCtrl.delete(id)