#_*_conding:utf-8_*_
# encoding=utf-8
from flask import render_template, request
from XiamiAutoSignin import app, db
from models import User
from sqlalchemy.exc import DBAPIError
import urllib2
import urllib
import re

def login(email, pw):
    login_data_ = {
        'email': email,
        'password': pw,
        'LoginButton': '登录'}
    login_url = 'http://www.xiami.com/web/login'
    login_headers = {
        'Referer': 'http://www.xiami.com/web',
        'User-Agent': 'Chrome/35.0'}

    login_data = urllib.urlencode(login_data_)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor)
    urllib2.install_opener(opener)

    # 登录
    login_request = urllib2.Request(login_url, login_data, login_headers)
    login_response = urllib2.urlopen(login_request).read()

    if '验证码' in login_response:
        if '验证码错误' in login_response:
            #判断验证码输入错误，无用，暂时保留
            return 'v_error'
        elif 'email或者密码错误' in login_response:
            return 'error'
        elif 'email 不存在' in login_response:
            return 'no'
        else:
            return 'validate'
    elif 'email或者密码错误' in login_response:
        return 'error'
    elif 'email 不存在' in login_response:
        return 'no'
    else:
        return days('http:www.xiami.com/profile', 'http://www.xiami.com/web')

def days(headers_url, checkin_url):
    # 签到
    checkin_headers = {
        'Referer': headers_url,
        'User-Agent': 'chrome/35.0'}
    checkin_request = urllib2.Request(checkin_url, None, checkin_headers)
    checkin_response = urllib2.urlopen(checkin_request).read()

    # 检查签到结果
    days_pattern = re.compile(r'已连续签到(\d+)天')
    try:
        result_match = days_pattern.findall(checkin_response)[0]
        return -int(result_match)
    except:
        return checkin_response


def checkin_url(mid_response):
    # 获取签到连接
    url_pattern = re.compile(r'href="/web/checkin/id/(\d+)"')
    url_match = url_pattern.findall(mid_response)[0]
    return 'http://www.xiami.com/web/checkin/id/' + url_match


def checkin_status(email,pw):
    query_days = login(email,pw)
    status={'state':u'签到成功','content':''}
    if query_days=='validate':
        status['state']=u'签到失败'
        status['content']=u'请过一段时间再来尝试'
    elif query_days=='v_error':
        status['state']=u'签到失败'
        status['content']=u'验证码错误'
    elif query_days=='no':
        status['state']=u'签到失败'
        status['content']=u'登录失败，email不存在'
    elif query_days == 'error':
        status['state']=u'签到失败'
        status['content']=u'登录失败，请检查账号密码是否填写正确'
    elif query_days > 0:
        status['content']=u'已经签到%s天' % days('http://www.xiami.com/web', checkin_url(query_days))
    else:
        status['content']=u'已经签到%s天' % abs(query_days)
    return status

@app.route('/')
def auto_signin():
    return render_template('xiami.html')


@app.route('/checkin', methods=['GET', 'POST'])
def checkin():
    email = request.form['email']
    pw = request.form['password']

    status=checkin_status(email,pw)

    return render_template('show.html',status=status)