#_*_conding:utf-8_*_
from flask import Flask
from flaskext.sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI

app=Flask(__name__)
# app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI']=SQLALCHEMY_DATABASE_URI

class nullpool_SQLAlchemy(SQLAlchemy):
	def apply_driver_hacks(self, app, info, options):
		super(nullpool_SQLAlchemy, self).apply_driver_hacks(app, info, options)
		from sqlalchemy.pool import NullPool
		options['poolclass'] = NullPool
		del options['pool_size']

db= nullpool_SQLAlchemy(app)

#db= SQLAlchemy(app)

import views,models

