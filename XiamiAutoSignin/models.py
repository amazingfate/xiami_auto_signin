#_*_conding:utf-8_*_
# encoding=utf-8
from XiamiAutoSignin import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    # 签到时间
    days = db.Column(db.Integer, nullable=False)
    #判断账号是否有效
    valid= db.Column(db.Boolean,nullable=False)


    def __init__(self, email, pw, days, valid):
        self.email = email
        self.password = pw
        self.days = days
        self.valid = valid

    def __repr__(self):
        return '<User %r>' % self.email

class OperatorDB:
    def query_all(self):
        return User.query.all()

    def filter_email(self,em):
        return User.query.filter_by(email=em).first()

    def updata_valid(self,uid,uvalid):
        user=User.query.filter_by(id=uid).first()
        user.valid=uvalid
        db.session.commit()

OperatorDB=OperatorDB()