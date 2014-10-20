# 虾米自动签到

实现虾米自动签到的一个小工具
LINK：[虾米自动签到](http://www.xiamias.sinaapp.com)

##代码说明

 - 使用语言：python
 - 使用urllib&urllib2模块模拟登陆，签到（为了简单方便，处理的是[web](http://www.xiami.com/web)页面）
 - 网站后台使用[flask](http://flask.pocoo.org/)搭建而成，运行于[sae](http://sae.sina.com.cn/)平台
 - 使用[sqlalchemy](http://www.sqlalchemy.org/)连接mysql，并且使用了[flask-sqlalchemy](https://pythonhosted.org/Flask-SQLAlchemy/)扩展
 - 前端使用的是[bootstrap](https://github.com/twbs/bootstrap)框架,基于[grayscale](http://startbootstrap.com/templates/grayscale/)模板修改而成
 - 使用ajax完成数据交互，提示使用的是[noty jQuery插件](https://github.com/needim/noty)
 
##使用方法
 
 
- 在输入框里输入虾米的账号和密码就行，没有登录过的账号系统会自己收录在数据库，登陆过的会直接返回签到结果
- 若是登记过账号后改过密码，在重新去网站登记就行
- 登记过账号之后系统每天会自动帮每个号签到

##其他

XiamiAutoSignin文件可以独立实现虾米账号的签到，只需要在文件结尾加上：

    checkin_status(your email,your password)
    
 就能实现签到功能

##TO DO

-- 完善后台管理功能
-- 验证码问题