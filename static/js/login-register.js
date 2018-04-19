/**
 * Created by liuliangjun on 2017/4/24.
 */

$(function(){
        $('.reset-btn').click(function(){
            $('input').val('')
        })

    //   登录
        $('.submit-login').click(function () {
            name = $('#username').val()
            pw = $('#pw').val()
            if (name == '' | pw == ''){
                UIkit.notify('用户名或密码不能为空！', {status: 'danger', timeout: 1500});
                return false
            }
            $.ajax({
                type: 'get',
                url: '/login',
                data: {
                    'username': name,
                    'pw': pw
                },
                success: function (msg) {
                    UIkit.notify(msg.msg, {status: msg.type, timeout: 1500});
                    if (msg.type == 'success'){
                        setTimeout(function(){
                            $('form').submit()
                        }, 1500)
                    }
                }
            })
        })

    //    注册
        $('.submit-register').click(function(){
            name = $('#username').val()
            pw = $('#pw').val()
            rpw = $('#rpw').val()
            if (name == '' | pw == '' | rpw == ''){
                UIkit.notify('用户名或密码不能为空！', {status: 'danger', timeout: 1500});
                return false
            }
            if (pw != rpw){
                UIkit.notify('两次输入密码不一致！', {status: 'danger', timeout: 1500});
                return false
            }
            $.ajax({  // 使用ajax异步提交注册信息
                type: 'get',
                url: '/register',
                data: {
                    'username': name,
                    'pw': pw,
                    'rpw': rpw
                },
                success: function (msg) {
                    UIkit.notify(msg.msg, {status: msg.type, timeout: 1500});
                    if (msg.type == 'success'){
                        setTimeout(function(){
                            $('form').submit()
                        }, 1500)
                    }
                }
            })
        })
    })
