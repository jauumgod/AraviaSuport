from app import app, db, UserMixin



class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255))
    password = db.Column(db.String(255), nullable=False)
    permissao = db.Column(db.String(10), nullable=False)