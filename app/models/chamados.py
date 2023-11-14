from app import app, db, datetime
from sqlalchemy import event




class Chamados(db.Model):
    sequencia_id = db.Column(db.Integer, primary_key = True)
    titulo =  db.Column(db.String(100), nullable=False)
    problema = db.Column(db.String(100), nullable=False)
    nivel = db.Column(db.String(100), nullable=False)
    data_create = db.Column(db.DateTime, default=datetime.utcnow())
    data_closed = db.Column(db.String(100))
    status = db.Column(db.String(20), nullable=False)
    comentario = db.Column(db.String(255))
    aberto_por = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    assumido_por = db.Column(db.String(255))
    fechado_por = db.Column(db.String(255))


