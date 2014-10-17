#_*_conding:utf-8_*_
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI

app=Flask(__name__)
# app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI']=SQLALCHEMY_DATABASE_URI
db=SQLAlchemy(app)


import views,models

