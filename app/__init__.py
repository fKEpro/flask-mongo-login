from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = MongoEngine()
db.init_app(app)

lm = LoginManager()
lm.init_app(app)

from app import views