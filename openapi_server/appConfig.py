import os
import connexion
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Nim96chathu@@localhost:13306/petstore'

connex_app = connexion.App(__name__, specification_dir='./openapi/')
app=connex_app.app

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Nim96chathu@@localhost:13306/petstore'

db = SQLAlchemy(app)
ma = Marshmallow(app)
# db.init_app(app)


