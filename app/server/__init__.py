import secrets
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.server.config.config import Config

app = Flask(__name__, static_folder='../public', template_folder="../views")
app.secret_key = secrets.token_hex(16)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/error/404.jinja'), 404
