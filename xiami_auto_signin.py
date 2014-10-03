#coding=utf-8
import urllib2
import urllib
import re

login_url = 'http://www.xiami.com/web/login'

login_data= urllib.urlencode({
	'email':'your email',
	'password':'your password',
	#'登录'的utf-8编码
	'LoginButton':'\xe7\x99\xbb\xe9\x99\x86',
	})

login_data=login_data.decode('utf-8')

login_headers={
	'Referer':'http://www.xiami.com/web',
	'User-Agent':'Chrome/35.0',
	}

opener=urllib2.build_opener(urllib2.HTTPCookieProcessor)
urllib2.install_opener(opener)

#登录
login_request=urllib2.Request(login_url,login_data,login_headers)
login_response=urllib2.urlopen(login_request).read()


#跳转到签到页
mid_headers={'Referer':'http:www.xiami.com/profile','User-Agent':'chrome/35.0'}
mid_request=urllib2.Request('http://www.xiami.com/web',None,mid_headers)
mid_response=urllib2.urlopen(mid_request).read()


#检查签到情况
days_pattern=re.compile(r'已连续签到(\d+)天')
if days_pattern.findall(mid_response):
	result_match=days_pattern.findall(mid_response)[0]
	print(u'成功！'+u'已经签到'+result_match+u'天')
else:
	#获取签到连接
	url_pattern=re.compile(r'href="/web/checkin/id/(\d+)"')
	try:
		url_match = url_pattern.findall(mid_response)[0]
	except StandardError,e:
		print (u'账户名或者密码错误，请重新填写')
	else:
		print url_match
		checkin_url = 'http://www.xiami.com/web/checkin/id/' + url_match

		#签到
		checkin_headers = {'Referer':'http://www.xiami.com/web', 'User-Agent' : 'chrome/35.0'}
		checkin_request= urllib2.Request(checkin_url,None,checkin_headers)
		checkin_response=urllib2.urlopen(checkin_request).read().decode('utf-8')

		#检查签到结果
		days_pattern = re.compile(r'已连续签到(\d+)天')
		if days_pattern:
			result_match=days_pattern.findall(checkin_response)[0]
			print (u'签到成功！'+u'已经签到'+result_match+u'天')
		else:
			print('fail！')
