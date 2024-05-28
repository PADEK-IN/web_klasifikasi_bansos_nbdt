from datetime import datetime
from app.server import db

class Warga(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nik = db.Column(db.String(16), index=True, unique=True, nullable=False)
    nama = db.Column(db.String(50), nullable=False)
    alamat = db.Column(db.String(150), nullable=False)
    no_rt = db.Column(db.Integer, nullable=False)
    pekerjaan = db.Column(db.String(70), nullable=False)
    penghasilan = db.Column(db.Numeric(10, 2), nullable=False, default=0.00)
    tanggungan = db.Column(db.Integer, nullable=False, default=0)
    kondisi_rumah = db.Column(db.Enum('Bambu Anyam', 'Papan', 'Batu Semen', 'Batu Permanen', name='role_enum'), nullable=False, default='Batu Permanen')
    status_rumah = db.Column(db.Enum('Sewa', 'Milik Sendiri', name='role_enum'), nullable=False, default='Sewa')
    jenis = db.Column(db.Enum('Miskin Extreme', 'PKH', 'CBP', 'Tidak Layak', 'Pending', name='role_enum'), nullable=False, default='Pending')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # email = db.Column(db.String(70), db.ForeignKey(User.email, onupdate='CASCADE', ondelete='SET NULL'))
    
    def __repr__(self):
        return '<Warga {}>'.format(self.name)