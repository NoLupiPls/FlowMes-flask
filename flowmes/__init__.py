from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_moment import Moment
from flask_mail import Mail
from flask_socketio import SocketIO
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'nl1authority@gmail.com'
app.config['MAIL_PASSWORD'] = '${{ MAIL_PASSWORD }}'
db = SQLAlchemy(app)
mail = Mail(app)
migrate = Migrate(app, db, render_as_batch=True)
bootstrap = Bootstrap(app)
login = LoginManager(app)
login.login_view = 'login'
moment = Moment(app)
socketio = SocketIO(app)

from flowmes import models, routes, errors
