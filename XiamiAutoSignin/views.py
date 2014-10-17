#_*_conding:utf-8_*_
# encoding=utf-8
from flask import render_template, request, jsonify, json
from XiamiAutoSignin import app, db
from models import User
from checkin import checkin_status


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/checkin', methods=['POST'])
def checkin():
    if request.method == 'POST':
        data = json.loads(request.form.get('data'))
        email = data['email']
        pw = data['password']
        print email
        print pw

        status = checkin_status(email, pw)
        user = User.query.filter_by(email=email).first()
        if user:
            # 已经登记过
            if status['state'] == u'success':
                user.days = int(status['content'])
                db.session.commit()
                status['content'] = u'已经登记，已签到%s天' % user.days
                if user.valid is False:
                    user.password = pw
                    user.valid = True
                    db.session.commit()
        else:
            if status['state'] == u'success':
                checkin_days = int(status['content'])
                user = User(email, pw, checkin_days, True)
                db.session.add(user)
                db.session.commit()
                status['content'] = u'登记成功，已签到%s天' % user.days

        print status
        return jsonify(result=status)


@app.route('/task')
def task():
    message = []
    user_len = 0
    status = {'id': '', 'email': '', 'state': '',
              'content': '', 'valid': '', 'tr_class': ''}

    user = User.query.all()
    if user:
        user_len = len(user)
        for i in xrange(user_len):
            # 只登陆有效的账号
            if user[i].valid == True:
                c_status = checkin_status(user[i].email, user[i].password)
                if c_status['state'] == 'error':
                    user.valid = False
                    db.commit()
                status = {'id': i + 1,
                          'email': user[i].email,
                          'state': c_status['state'],
                          'content': u'已经签到%s天' % c_status['content'],
                          'valid': u'有效',
                          'tr_class': 'success'}
            else:
                status = {'id': i + 1,
                          'email': user[i].email,
                          'state': u'失效',
                          'content': u'登记失效',
                          'valid': u'无效',
                          'tr_class': 'error'}
            message.append(status)

    return render_template('task.html', user_len=user_len, message=message)