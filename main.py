from app.server import app

from app.server.routes import dosen, mahasiswa
from app.server.routes.auth.auth_router import Auth

app.register_blueprint(Auth)
app.register_blueprint(dosen.Dosen,url_prefix="/dosen")
app.register_blueprint(mahasiswa.Mahasiswa,url_prefix="/mahasiswa")
