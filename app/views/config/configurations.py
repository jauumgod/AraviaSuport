from app import *


@login_required
@app.route("/configurations")
def configurations():
    return render_template("conf/config.html")