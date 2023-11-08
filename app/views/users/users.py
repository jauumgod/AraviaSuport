from app import *
from ...models.usuarios import Usuario


@login_required
@app.route("/usuarios")
def usuarios():
    db = Usuario.query.all()
    return render_template("usuarios/usuarios.html", result = db)


@login_required
@app.route("/change_permission/<int:id>", methods=['GET', 'POST'])
def change_permission(id):
    if request.method == 'POST':    
        query = Usuario.query.filter_by(id=id).first()
        nova_permissao = request.form['select']
        query.permissao = nova_permissao
        db.session.commit()
        time.sleep(1)
        
    return redirect(url_for("usuarios"))