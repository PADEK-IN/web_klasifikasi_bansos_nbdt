from flask import Blueprint, render_template, request, redirect
from app.server.routes.auth import auth_controller

# Auth = Blueprint('auth', __name__, template_folder="../../../views") <-- jika ingin menginisialisasi sendiri root folderya
Auth = Blueprint('auth', __name__)

@Auth.route('/')
def index():
    return render_template("index.jinja", title="Flask and Jinja")

@Auth.route('/register', methods=["GET", "POST"])
def register():
    nameType = [
        {"type": "text", "name":"name", "text": "Name"},
        {"type": "email", "name":"email", "text": "Email"},
        {"type": "password", "name":"password", "text": "Password"},
        {"type": "password", "name":"confirmPassword", "text": "Confirm Password"}
    ]
    if request.method == "GET":
        return render_template('pages/auth/register.jinja', title="Register", nameType=nameType)
    else:
        auth_controller.register()
        return redirect("/login")

@Auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('pages/auth/login.jinja', title="Login")
    else:
        auth_controller.login()
        return render_template("index.jinja", title="Flask and Jinja")

@Auth.route("/logout", methods=["GET"])
def logout():
    auth_controller.logout()
    return redirect("/login")