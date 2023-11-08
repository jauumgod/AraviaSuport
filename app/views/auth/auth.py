from app import *
from ...models.usuarios import Usuario
import datetime

login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))




@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        usuario = request.form['usuario']
        senha = request.form['senha']

        user = Usuario.query.filter_by(username=usuario).first()

        if not user or not check_password_hash(user.password, senha):
            flash("Usuario ou senha incorretos")
            return redirect(url_for("login"))
        
        login_user(user, duration=datetime.timedelta(days=1))
        time.sleep(1)
        return redirect(url_for('homepage'))

    
    return render_template("auth/login.html")


@login_required
@app.route("/cadastro", methods=['GET', 'POST'])
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



@login_required
@app.route("/logout")
def logout():
    logout_user()
    time.sleep(1)
    return redirect(url_for("login"))