from flask import Flask, render_template, url_for, redirect, request, flash
from flask_login import current_user, AnonymousUserMixin,LoginManager, login_manager, UserMixin, login_required, login_user, logout_user
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime, timedelta
import time
import psycopg2



app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy()
mi = Migrate(app, db)
db.init_app(app)
login_manager = LoginManager(app)
login_manager.init_app(app)


from .models import usuarios, chamados
from .views.auth import auth
from .views.chamados import chamados
from .views.config import configurations
from .views.users import users
from .controller import my_functions