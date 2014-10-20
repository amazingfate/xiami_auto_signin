#_*_conding:utf-8_*_
from flaskext.sqlalchemy import SQLAlchemy
from flask import Flask
from setting import MYSQL_USER,MYSQL_PASS,MYSQL_HOST_M,MYSQL_HOST_S,MYSQL_PORT,MYSQL_DB

app=Flask(__name__)
app.debug=True

app.secret_key = 'k4hp8ri1ng$@nbwqk+(fhdshgn9sR~XHH!jmN]LWX/,?RT'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s:%s/%s?charset=utf8' % (MYSQL_USER,MYSQL_PASS,MYSQL_HOST_M,MYSQL_PORT,MYSQL_DB)

class nullpool_SQLAlchemy(SQLAlchemy):
	def apply_driver_hacks(self, app, info, options):
		super(nullpool_SQLAlchemy, self).apply_driver_hacks(app, info, options)
		from sqlalchemy.pool import NullPool
		options['poolclass'] = NullPool
		del options['pool_size']


db=nullpool_SQLAlchemy(app)


import views,models

