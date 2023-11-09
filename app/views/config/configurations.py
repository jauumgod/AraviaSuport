from app import *
from ...models.usuarios import UsuarioAutenticado, Usuario
from ...controller.my_functions import gerar_token_aleatorio

@app.route("/configurations")
@login_required
def configurations():
    usuarios_conectados = UsuarioAutenticado.query.all()
    return render_template("conf/config.html", response = usuarios_conectados)




