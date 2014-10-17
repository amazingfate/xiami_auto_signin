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

function generate(text) {
    var n = noty({
        text        : text,
        type        : 'error',
        dismissQueue: true,
        layout      : 'center',
        theme       : 'jian'
    });
}
// 表单非空检查
function validate_required(field,alerttxt)
{
    with (field)
      {
          if (value==null||value=="")
            {generate(alerttxt);return false}
          else {return true}
      }
}

//email格式检查
function validate_email(field,alerttxt)
{
    with (field)
    {
        apos=value.indexOf("@")
        dotpos=value.lastIndexOf(".")
        if (apos<1||dotpos-apos<2) 
          {generate(alerttxt);return false}
        else {return true}
    }
}


$("form").submit(function() {
    if (validate_email(email,"请输入正确的email地址!")==false)
        {email.focus();return false}
    if (validate_required(password,"密码不能为空!")==false)
        {password.focus();return false}
    alert('ajax')
});