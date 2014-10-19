// jQuery to collapse the navbar on scroll
$(window).scroll(function() {
    if ($(".navbar").offset().top > 50) {
        $(".navbar-fixed-top").addClass("top-nav-collapse");
    } else {
        $(".navbar-fixed-top").removeClass("top-nav-collapse");
    }
});

// jQuery for page scrolling feature - requires jQuery Easing plugin
$(function() {
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });
});

// Closes the Responsive Menu on Menu Item Click
$('.navbar-collapse ul li a').click(function() {
    $('.navbar-toggle:visible').click();
});

$(document).ready(function() {
    //noty js 提示
    var generate = function(type, text) {
        var n = noty({
            text: text,
            type: type,
            dismissQueue: true,
            layout: 'center',
            theme: 'jian'
        });
    };

    //email格式检查
    var validate_email = function(field, alerttxt) {
        with(field) {
            apos = field.val().indexOf("@")
            dotpos = field.val().lastIndexOf(".")
            if (apos < 1 || dotpos - apos < 2) {
                generate('warning', alerttxt);
                return false
            } else {
                return true
            }
        }
    };

    // 表单非空检查
    var validate_required = function(field, alerttxt) {
        with(field) {
            if (field.val() == null || field.val() == "") {
                generate('warning', alerttxt);
                return false
            } else {
                return true
            }
        }
    };

    //ajax部分
    var submit_ajax = function(e) {
        var data = {
            data: JSON.stringify({
                "email": $('input[name="email"]').val(),
                "password": $('input[name="password"]').val()
            })
        };
        $.ajax({
            url: $SCRIPT_ROOT + '/checkin',
            type: 'POST',
            data: data,
            success: function(data) {
                generate(data.result['state'], data.result['content']);
                $('span#password').text("");
            }
        });
        return false
    };

    var submit_form = function() {
        if (validate_email($('input[name="email"]'), "请输入正确的email地址!") == false) {
            email.focus();
            return false;
        };
        if (validate_required($('input[name="password"]'), "密码不能为空!") == false) {
            password.focus();
            return false;
        };
        submit_ajax()
    };

    $('a[name="checkin"]').bind('click', submit_form);
});