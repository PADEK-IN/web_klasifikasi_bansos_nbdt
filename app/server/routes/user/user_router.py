from flask import Blueprint, render_template, session, redirect
from app.server.routes.user import user_controller

User = Blueprint('user', __name__)

@User.route("/user")
def user():
    if 'login' in session:
        dataUser = user_controller.allData()
        if not dataUser:
            return render_template("pages/error/500.jinja")
        return render_template("pages/user/list.jinja", name=session['name'], data=dataUser)
    else:
        return redirect('/login')