from flask import request
from flask import session
from app.server import db
from app.server.model.user import User
from app.server.helper import response
from app.server.helper.formating import dataUser


def register():
    try:
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        confirmPassword = request.form.get("confirmPassword")

        if password != confirmPassword:
            return response.badReq([], "Maaf password yang anda masukkan tidak sama")

        newUser = User(name=name, email=email)
        newUser.setPassword(password)

        db.session.add(newUser)
        db.session.commit()

        return response.successCreated("Berhasil registrasi")
    except Exception as e:
        print(e)
        return response.serverError()


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

        session["id"] = data["id"]
        session["email"] = data["email"]

        result = {"data": data}

        return response.success(result, "Yeay anda berhasil login")
    except Exception as e:
        print(e)
        return response.serverError()


def logout():
    try:
        session.pop("id", None)
        session.pop("email", None)

        return True
        # return response.success(None, "Anda berhasil logout")
    except Exception as e:
        print(e)
        return response.serverError()
