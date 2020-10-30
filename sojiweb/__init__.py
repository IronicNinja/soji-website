from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
import os
from .models import RealMessage, EmailList

app = Flask(__name__)
app.config.from_pyfile('config.py')

#protect against malicious attacks
db = SQLAlchemy(app)
mail = Mail()
mail.init_app(app)

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()

from sojiweb import routes