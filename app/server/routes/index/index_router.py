from flask import Blueprint, render_template
from app.server.routes.index import index_controller

Index = Blueprint('index', __name__)

@Index.route('/')
def index():
    result = index_controller.count()
    return render_template("pages/index/index.jinja", name="Admin", count=result)

@Index.route('/profile')
def profile():
    return render_template("pages/index/profile.jinja", name="Admin")