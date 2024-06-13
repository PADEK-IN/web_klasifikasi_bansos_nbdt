from flask import Blueprint, render_template, session, redirect
from app.server.routes.index import index_controller

Index = Blueprint('index', __name__)

@Index.route('/')
def index():
    if 'login' in session:
        result = index_controller.count()
        return render_template("pages/index/index.jinja", name=session['name'], count=result)
    else:
        return redirect('/login')

# @Index.route('/profile')
# def profile():
#     return render_template("pages/index/profile.jinja", name="Admin")