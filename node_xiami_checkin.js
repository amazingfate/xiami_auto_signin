var superagent = require('superagent');
var cheerio = require('cheerio');

//负责查询签到连接或者签到天数
function UrlOrDays(res,ud) {
    var $ = cheerio.load(res);
    var checkin = [];
    $('.idh').each(function (idx, element) {
        var $element = $(element);
        if (ud) {
            //查找连接
            checkin.push($element.find('a').attr('href'));
        } else {
            //查询签到状态
            checkin.push($element.text());
        }
    });
    return checkin;
}

//登录成功后查询签到情况
function checkin(url,cookie) {
    var agent = superagent.agent();
    agent
    .get(url)
    .set({ 'cookie': cookie })
    .end(function (err, res) {
            if (err) {
                console.log(err);
            }
            var url = UrlOrDays(res.text, true);
            _url = 'http://www.xiami.com' + url[1];
            if (url[1]) {
                //未签到，访问签到连接，此处的模拟浏览器点击的没有完成
                checkin(_url,cookie);
            } else {
                //已经签到
                console.log(UrlOrDays(res.text,false)[1]);
            }
        });
}

function xiami(email,pw){
    var agent = superagent.agent();
    agent
    .post('http://www.xiami.com/web/login')
    .type('form')
    .send({ 'email':email, 'password': pw , 'LoginButton': '登录' })
    .end(function (err, sres) {
            if (err) {
                return next(err);
            }
            var $ = cheerio.load(sres.text);
            //通过检查一个class=header的div下面有无a标签来判断登录成功与否
            $('.header').each(function (i, e) {
                var aa = $(e).find('a').attr('href');
                if (aa) {
                    //登录成功
                    checkin('http://www.xiami.com/web',sres.req._headers['cookie']);
                } else {
                    //登录不成功，输出错误提示
                    var land = $('.land').find('p > b').text();
                    console.log(land);
                }
       });
    });
}

xiami('your email','your password');