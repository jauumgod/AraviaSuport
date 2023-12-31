from app import *
from ...models.chamados import Chamados



@app.route("/home")
@login_required
def homepage():    
    return render_template('home/homepage.html')


@app.route("/abrir_chamados", methods=['GET', 'POST'])
@login_required
def abrir_chamados(): 
    if request.method == 'POST':
        chamado = Chamados()
        chamado.titulo = request.form['titulo']
        chamado.problema = request.form['problema']
        chamado.nivel = request.form['nivel']
        chamado.data_closed = "None"
        chamado.status = "Aberto"
        chamado.aberto_por = current_user.username
        db.session.add(chamado)
        db.session.commit()
        time.sleep(1)
        flash("chamado aberto com sucesso!")
    return render_template('chamados/abrir_chamado.html')



@app.route("/chamados")
@login_required
def chamados():
    query = Chamados.query.all()
    return render_template('chamados/chamados.html', result=query)



@app.route("/chamados/<int:id>")
@login_required
def chamados_id(id):
    query = Chamados.query.filter_by(sequencia_id=id).first()
    return render_template('chamados/chamado.html', result=query)


@app.route("/fechados")
@login_required
def fechados():
    query = Chamados.query.filter(Chamados.fechado_por!= "").all()
    return render_template("chamados/fechados.html", result=query)


@app.route("/assumir_chamados/<int:id>")
def assumir_chamados(id):
    ch = Chamados()
    chamados_query = Chamados.query.filter_by(sequencia_id = id).first()
    chamados_query.assumido_por = current_user.username
    db.session.add(chamados_query)
    db.session.commit()
    flash(f"Chamado por {current_user.username}, assumido com sucesso!")
    redirect(url_for('chamados'))
    return redirect(url_for("chamados_id", id=id))

@app.route("/fechar_chamados/<int:id>")
def fechar_chamados(id):
    ch = Chamados()
    chamados_query = Chamados.query.filter_by(sequencia_id = id).first()
    chamados_query.fechado_por = current_user.username
    db.session.add(chamados_query)
    db.session.commit()
    flash(f" Chamado fechado com sucesso!")
    redirect(url_for('chamados'))

    return redirect(url_for("chamados_id", id=id))


