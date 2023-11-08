from app import *
from ...models.chamados import Chamados

@login_required
@app.route("/home")
def homepage():
    return render_template('home/homepage.html')

@login_required
@app.route("/abrir_chamados", methods=['GET', 'POST'])
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
def chamados():
    query = Chamados.query.all()
    return render_template('chamados/chamados.html', result=query)



@app.route("/chamados/<int:id>")
def chamados_id(id):
    query = Chamados.query.filter_by(sequencia_id=id).first()
    return render_template('chamados/chamado.html', result=query)


@app.route("/fechados")
def fechados():
    status = "fechado"
    query = Chamados.query.filter_by(status=status).first()
    return render_template("chamados/fechados.html", result=query)