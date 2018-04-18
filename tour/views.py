# coding:utf-8
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, HttpResponse, render_to_response
from django.contrib.auth import authenticate, login, logout
from models import *
import random
import json


def init(request):
    return render(request, 'index.html')


def detail(request):
    return render(request, 'detail.html')


@csrf_exempt
def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username', False)
        pw = request.POST.get('pw', False)
        user = authenticate(username=username, password=pw)
        print username, pw
        print user
        if user:
            login(request, user)
            return redirect('/')

    if request.method == 'GET':
        username = request.GET.get('username', False)
        pw = request.GET.get('pw', False)
        if not username or not pw:
            return render(request, 'login.html')
        user = authenticate(username=username, password=pw)
        msg = {
            'msg': u'登录成功，页面正在跳转！',
            'type': 'success'
        }
        if not user:
            msg['msg'] = u'账号或密码错误,请检查后重新登录!'
            msg['type'] = 'danger'
        return HttpResponse(json.dumps(msg), content_type='application/json')


@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', False)
        pw = request.POST.get('pw', False)
        rpw = request.POST.get('rpw', False)

        # 生成随机编号
        number = random.randint(1000000, 9999999)
        if not ExtUser.objects.filter(number=number):
            user = User.objects.create_user(username=username, password=pw)
            ExtUser.objects.create(user=user, number=number)
            user = authenticate(username=username, password=pw)
            login(request, user)
            return redirect('/')

    elif request.method == 'GET':
        username = request.GET.get('username', False)
        pw = request.GET.get('pw', False)
        rpw = request.GET.get('rpw', False)
        if not username or not pw:
            return render(request, 'register.html')
        msg = {
            'msg': u'账号注册成功!',
            'type': 'success'
        }
        if not pw.isalnum():
            msg['msg'] = u'密码只能由数字字母组成！'
            msg['type'] = 'danger'
        if pw != rpw:
            msg['msg'] = u'两次输入的密码不一致！'
            msg['type'] = 'danger'
        if len(pw) < 6:
            msg['msg'] = u'密码至少需要6个字符！'
            msg['type'] = 'danger'
        if User.objects.filter(username=username):
            msg['msg'] = u'用户名已经存在！'
            msg['type'] = 'danger'

        return HttpResponse(json.dumps(msg), content_type='application/json')


def sign_out(request):
    logout(request)
    return redirect('/')
