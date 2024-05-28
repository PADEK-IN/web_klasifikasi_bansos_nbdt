from flask import Blueprint, request, render_template, redirect
from app.server.routes.user import user_controller

User = Blueprint('user', __name__)

@User.route("/user")
def user():
    return render_template("pages/user/list.jinja")
