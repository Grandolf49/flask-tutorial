from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flaskblog.forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'da2c057395b3f3e5ca728f4f688da59e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from flaskblog import routes
