from flask import request, session
from app.server import db
from app.server.model.user import User
from app.server.helper import response
from app.server.helper.formating import dataUser


def register():
    try:
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        newUser = User(name=name, email=email)
        newUser.setPassword(password)

        db.session.add(newUser)
        db.session.commit()

        return True
    except Exception as e:
        print(e)
        return False


def login():
    try:
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if not user:
            return response.badReq([], "Maaf user tidak ditemukan")

        if not user.verifyPassword(password):
            return response.unAuth("Maaf password yang anda masukkan salah")

        data = dataUser(user)

        session["login"] = True
        session["name"] = data["name"]
        session["email"] = data["email"]

        return True
    except Exception as e:
        print(e)
        return False

def logout():
    try:
        # session.pop("login", None)
        # session.pop("name", None)
        # session.pop("email", None)
        session.clear()
        return True
    except Exception as e:
        print(e)
        return False
