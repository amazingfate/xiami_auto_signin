#_*_conding:utf-8_*_
# coding=utf-8
import urllib2
import urllib
import re


def login(email,pw):
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


    if 'email或者密码错误' in login_response:
        return 0
    else:
        return days('http:www.xiami.com/profile','http://www.xiami.com/web')

def days(headers_url,checkin_url):
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

def checkin(mid_response):
    # 获取签到连接
    url_pattern = re.compile(r'href="/web/checkin/id/(\d+)"')
    url_match = url_pattern.findall(mid_response)[0]
    return 'http://www.xiami.com/web/checkin/id/' + url_match



query_days=login('your email','your password')
if query_days>0:
    print (u'已经签到%s天'%days('http://www.xiami.com/web',checkin(query_days)))
elif query_days== 0:
    print(u'登录失败，请检查账号密码是否填写正确')
else:
    print (u'已经签到%s天'%abs(query_days))