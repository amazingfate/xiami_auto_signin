#_*_ coding utf-8 _*_
import urllib2
import urllib

login_url = 'http://www.xiami.com/web/login'

login_data= urllib.urlencode({
	'email':'740230453@qq.com',
	'password':'wilson1950',
	#'登录'的unicode码
	'LoginButton':'\xe7\x99\xbb\xe9\x99\x86',
	})

print (login_data)

login_data=login_data.decode('utf-8')

print (login_data)

login_headers={
	'Referer':'http://www.xiami.com/web',
	'User-Agent':'Chrome/35.0',
}

opener=urllib2.build_opener(urllib2.HTTPCookieProcessor)
urllib2.install_opener(opener)

login_request=urllib2.Request(login_url,login_data,login_headers)
login_reponse=urllib2.urlopen(login_request).read().decode('utf-8')


login_reponse=login_reponse.decode('utf-8').encode('gbk')

with open('xiami.html','w') as f:
	f.write(login_reponse)
f.close()

print ('done')
