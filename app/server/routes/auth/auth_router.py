from flask import Blueprint, render_template, request, redirect, session
from app.server.routes.auth import auth_controller

Auth = Blueprint('auth', __name__)

@Auth.route('/register', methods=["GET", "POST"])
def register():
    if 'login' in session:
        return redirect('/')
    else:
        if request.method == "GET":
            return render_template('pages/auth/register.jinja')
        if request.method == "POST":
            regis = auth_controller.register()
            if not regis:
                return render_template("pages/error/auth500.jinja")
            return redirect("/login")

@Auth.route("/login", methods=["GET", "POST"])
def login():
    if 'login' in session:
        return redirect('/')
    else:
        if request.method == "GET":
            return render_template('pages/auth/login.jinja')
        if request.method == "POST":
            signin = auth_controller.login()
            if not signin:
                return render_template("pages/error/auth500.jinja")
            return redirect("/")

@Auth.route("/logout")
def logout():
    if 'login' in session:
        auth_controller.logout()
        return redirect("/login")
    else:
        return redirect('/login')