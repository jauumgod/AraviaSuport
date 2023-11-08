from app import app, db, datetime



class Chamados(db.Model):
    sequencia_id = db.Column(db.Integer, primary_key = True)
    titulo =  db.Column(db.String(100), nullable=False)
    problema = db.Column(db.String(100), nullable=False)
    nivel = db.Column(db.String(100), nullable=False)
    data_create = db.Column(db.DateTime, default=datetime.utcnow())
    data_closed = db.Column(db.String(100))
    status = db.Column(db.String(20), nullable=False)
    aberto_por = db.Column(db.Integer, db.ForeignKey('usuario.id'))
