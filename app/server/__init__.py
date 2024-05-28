import secrets
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.server.config.config import Config

app = Flask(__name__, template_folder="../views")
app.secret_key = secrets.token_hex(16)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

