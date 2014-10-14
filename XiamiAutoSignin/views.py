#_*_conding:utf-8_*_
# encoding=utf-8
from flask import render_template, request
from XiamiAutoSignin import app, db
from models import User
from checkin import checkin_status
# from sqlalchemy.exc import DBAPIError


@app.route('/')
def auto_signin():
    return render_template('xiami.html')


@app.route('/checkin', methods=['GET', 'POST'])
def checkin():
    email = request.form['email']
    pw = request.form['password']

    status = checkin_status(email, pw)
    user = User.query.filter_by(email=email).first()
    if user:
    # 已经登记过
        if status['state'] == u'签到成功':
            status['state'] = u'已经登记'
            user.days=int(status['content'])
            db.session.commit()
            if user.valid is False:
                user.password = pw
                user.valid=True
                db.session.commit()

    else:
        if status['state'] == u'签到成功':
            status['state'] = u'登记成功'
            checkin_days = int(status['content'])
            user = User(email, pw, checkin_days, True)
            db.session.add(user)
            db.session.commit()


    return render_template('show.html', status=status)

@app.route('/task')
def task():
    message=[]
    user_len=0
    status={'id':'','email':'','state':'','content':'','valid':'','tr_class':''}

    user=User.query.all()
    if user:
        user_len=len(user)
        for i in xrange(user_len):
            if user[i].valid==True:
                c_status = checkin_status(user[i].email,user[i].password)
                if c_status['state']==u'签到失败':
                    user.valid=False
                    db.commit()
                status={'id':i+1,
                'email':user[i].email,
                'state':c_status['state'],
                'content':u'已经签到%s天'%c_status['content'],
                'valid':u'有效',
                'tr_class':'success'}
            else:
                status={'id':i+1,
                'email':user[i].email,
                'state':u'失效',
                'content':u'登记失效',
                'valid':u'无效',
                'tr_class':'error'}
            message.append(status)

    return render_template('task.html',user_len=user_len,message=message)