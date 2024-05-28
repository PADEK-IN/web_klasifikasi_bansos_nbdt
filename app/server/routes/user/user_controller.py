from flask import request
from app.server import db
from app.server.model.user import User
from app.server.helper import response
from app.server.helper.formating import dataUser


def allData():
    try:
        data = User.query.all()

        if not data:
            return render_template("pages/error/400.jinja")

        result = dataUser(data)

        return result
        # return response.success(result, "Response Success")
    except Exception as e:
        print(e)
        return render_template("pages/error/500.jinja")
