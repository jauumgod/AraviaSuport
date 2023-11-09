from app import app, db, UserMixin


class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255))
    password = db.Column(db.String(255), nullable=False)
    permissao = db.Column(db.String(15), nullable=False)
    active = db.Column(db.Boolean)

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.is_active

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
    
class UsuarioAutenticado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    login_time = db.Column(db.DateTime)
    client_names = db.relationship('Usuario', backref=db.backref('names', lazy=True))