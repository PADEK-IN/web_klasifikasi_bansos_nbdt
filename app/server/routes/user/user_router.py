from flask import Blueprint, request, render_template, redirect
from app.server.routes.user import user_controller

User = Blueprint('user', __name__)

@User.route("/user", methods=["GET", "POST"])
def user():
    if request.method == "GET":
        return render_template("pages/user/list.jinja")
    elif request.method == "POST":
        return redirect('/user')
    else:
        return render_template("pages/error/400.jinja")
    
@User.route("/user/add", methods=["GET"])
def addMahasiswa():
    if request.method == "GET":
        return render_template("pages/user/add.jinja")
    else:
        return render_template("pages/error/400.jinja")
    
@User.route("/user/<id>", methods=["GET"])
def detailMhs(id):
    return render_template("pages/user/detail.jinja")
    
@User.route("/user/edit/<id>", methods=["GET", "POST"])
def editMhs(id):
    if request.method == "GET":
        return render_template("pages/user/edit.jinja")
    # elif request.method == "POST":
    #     return MhsCtrl.edit(id)
    else:
        return render_template("pages/error/400.jinja")
    
# @User.route("/user/delete/<id>", methods=["GET"])
# def deleteMhs(id):
#     return MhsCtrl.delete(id)