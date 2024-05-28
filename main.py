from app.server import app

from app.server.routes.auth.auth_router import Auth
from app.server.routes.index.index_router import Index
from app.server.routes.user.user_router import User
from app.server.routes.warga.warga_router import Warga
from app.server.routes.klasifikasi.klasifikasi_router import Klasifikasi

app.register_blueprint(Index)
app.register_blueprint(Auth)
app.register_blueprint(User)
app.register_blueprint(Warga, url_prefix="/warga")
app.register_blueprint(Klasifikasi)
