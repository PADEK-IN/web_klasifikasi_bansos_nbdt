from flask import Blueprint, render_template
from app.server.routes.user import user_controller

User = Blueprint('user', __name__)

@User.route("/user")
def user():
    dataUser = user_controller.allData()
    print(dataUser)
    if not dataUser:
        return render_template("pages/error/500.jinja")
    return render_template("pages/user/list.jinja", name="Admin", data=dataUser)
