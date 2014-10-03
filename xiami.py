#!/usr/bin/env python3
# -*- coding: utf-8 -*-

script_info='''
多账户虾米自动签到器
请在http://python.org/getit/ 下载python3.

作者：kK(fkfkbill@gmail.com)
http://kkblog.org
'''

from urllib.request import urlopen,install_opener,build_opener,Request,HTTPHandler,HTTPCookieProcessor
from http.cookiejar import CookieJar
from urllib.parse import urlencode


#在此填写账户名（可多账户）
user_info=[
	{"email":"","password":""},
]


#xiami uris
site_urls={
	"index":r"http://www.xiami.com/",
	"login":r"http://www.xiami.com/member/login",
	"signin":r"http://www.xiami.com/task/signin",
}

#login form without email and password
# (and will be filled when loggin-in)
login_form={
	"done":"/",
	"submit":"登 录",
}

#flags
site_flags={
	"logged-in":r"我的道具",
	"login-failed":"密码错误",
    "identify-required":"请输入验证码",
	"not-signed-in":"签到得体验点<span>",
	"signed-in":"天<span>已连续签到</span><",
}

headers={
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	"Accept-Encoding":"zip,deflate,sdch",
	"Accept-Language":"en-US,en;q=0.8",
	"Cache-Control":"max-age=0",
	"Connection":"keep-alive",
	"Host":"www.xiami.com",
	"Referer":"http://www.xiami.com/",
	"User-Agent":"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
}


#=========================
def login(n):
	'''
login xiami.
arugments:
	n:
return:
	url opener:when succeeded
	None:when failed or have signed in
'''
	cookie_support= HTTPCookieProcessor(CookieJar())
	opener = build_opener(cookie_support, HTTPHandler)
	install_opener(opener)

	lf=login_form
	lf.update(user_info[n])
	req=Request(url=site_urls["login"],data=urlencode(lf).encode("utf-8"),headers=headers)
	content=urlopen(req).read().decode("utf-8")
	
	if content.find(site_flags["signed-in"])!=-1:
		print("%s：已签过。\r\n"%user_info[n]["email"])
	elif content.find(site_flags["login-failed"])!=-1:
		print("%s：邮箱或密钥错误。\r\n"%user_info[n]["email"])
	elif content.find(site_flags["identify-required"])!=-1:
		print("%s：虾米要求输入验证码，请断网后重新尝试。\r\n"%user_info[n]["email"])
	elif content.find(site_flags["logged-in"])!=-1:
		print("%s：登录成功。"%user_info[n]["email"])
		return opener
	return None



#=========================
def signin(opener):
	'''
sign in xiami.com to get daily coins:P
arugments:
	opener:a urllib opener that is logged in xiami.com
return:
	True:succeeded
	False:failed.
'''
	if opener==None:return
	install_opener(opener)
	req=Request(url=site_urls["signin"],headers=headers)
	content=urlopen(req).read().decode("utf-8")
	
	req=Request(url=site_urls["index"],headers=headers)
	if urlopen(req).read().decode("utf-8").find(site_flags["signed-in"])!=-1:
		print("签到成功。\r\n")
		return True
	else:
		print("签到失败，请联系作者报bug，谢谢:P\r\n")
	return False



#=========================
if __name__=="__main__":
	print(script_info)
	for i in range(len(user_info)):
		signin(login(i))
	input("回车结束。谢谢使用嘻嘻:P")
