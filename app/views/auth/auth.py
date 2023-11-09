from app import *
from ...models.usuarios import Usuario, UsuarioAutenticado
import datetime

LIMITE_USUARIOS_POR_ID = 2

login_manager = LoginManager(app)


class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id



@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))



@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        usuario = request.form['usuario']
        senha = request.form['senha']

        user = Usuario.query.filter_by(username=usuario).first()

        if user and check_password_hash(user.password, senha):
            if verifica_limite_usuarios_por_id(user.id):
                flash("Limite de usuários com o mesmo ID atingido. Tente novamente mais tarde.")
            else:
                login_user(user, duration=datetime.timedelta(days=1))
                usuario_autenticado = UsuarioAutenticado(user_id=user.id, login_time=datetime.datetime.now(), username_logado=user.username )
                db.session.add(usuario_autenticado)
                db.session.commit()
                return redirect(url_for('homepage'))
        else:
            flash("Usuário ou senha incorretos")
    
    return render_template("auth/login.html")

def verifica_limite_usuarios_por_id(user_id):
    usuarios_com_mesmo_id = UsuarioAutenticado.query.filter_by(user_id=user_id).count()
    return usuarios_com_mesmo_id >= LIMITE_USUARIOS_POR_ID



@app.route("/cadastro", methods=['GET', 'POST'])
@login_required
def cadastro():
    if request.method == 'POST':
        user = Usuario()
        user.username = request.form['username']
        user.email = request.form['email']
        user.password = generate_password_hash(request.form['password'])
        user.permissao = request.form['select']
         
        query = Usuario.query.filter_by(username=user.username).first()

        if query:
            flash("Usuario Já existe")
            time.sleep(2)
            return redirect("usuarios")

        db.session.add(user)
        db.session.commit()
        flash('Usuario criado com sucesso!')
        time.sleep(2)
        return redirect(url_for("usuarios"))



@app.route("/logout")
@login_required
def logout():
    logout_user()
    time.sleep(1)
    return redirect(url_for("login"))



@app.route('/desconectar_usuario/<int:user_id>')
@login_required
def desconectar_usuario(user_id):
    usuario = UsuarioAutenticado.query.filter_by(user_id=user_id).first()
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        flash("Usuário desconectado com sucesso.")
        time.sleep(1)
    return redirect(url_for('configurations'))


@app.route('/excluir_usuario/<int:user_id>')
@login_required
def excluir_usuario(user_id):
    usuario = Usuario.query.filter_by(id=user_id).first()
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        flash("Usuário removido com sucesso.")
        time.sleep(1)
    return redirect(url_for('configurations'))