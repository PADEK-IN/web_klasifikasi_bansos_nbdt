from flask import request
from app.server import db
from app.server.model.user import User
from app.server.helper import response
from app.server.helper.formating import dataUserAll


def allData():
    try:
        data = User.query.all()

        if not data:
            return "empty"

        return dataUserAll(data)

    except Exception as e:
        print(e)
        return False
