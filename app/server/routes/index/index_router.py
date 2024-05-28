from flask import Blueprint, render_template, request, redirect
# from app.server.routes.index import index_controller

Index = Blueprint('index', __name__)

@Index.route('/')
def index():
    return render_template("pages/index/index.jinja", message="Selamat Datang Kanti")