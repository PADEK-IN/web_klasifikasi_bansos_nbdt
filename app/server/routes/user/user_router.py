from flask import Blueprint, request, render_template, redirect
from app.server.routes.user import user_controller

User = Blueprint('user', __name__)

@User.route("/user", methods=["GET", "POST"])
def user():
    if request.method == "GET":
        return render_template("pages/user/list.html")
    elif request.method == "POST":
        return redirect('/user')
    else:
        return render_template("pages/error/400.html")
    
@User.route("/user/add", methods=["GET"])
def addMahasiswa():
    if request.method == "GET":
        return render_template("pages/user/add.html")
    else:
        return render_template("pages/error/400.html")
    
@User.route("/user/<id>", methods=["GET"])
def detailMhs(id):
    return render_template("pages/user/detail.html")
    
@User.route("/user/edit/<id>", methods=["GET", "POST"])
def editMhs(id):
    if request.method == "GET":
        return render_template("pages/user/edit.html")
    # elif request.method == "POST":
    #     return MhsCtrl.edit(id)
    else:
        return render_template("pages/error/400.html")
    
# @User.route("/user/delete/<id>", methods=["GET"])
# def deleteMhs(id):
#     return MhsCtrl.delete(id)