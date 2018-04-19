# coding:utf-8
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, HttpResponse, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.forms.models import model_to_dict
from models import *
import random
import json


def init(request):
    if request.method == 'GET':
        # 热门推荐 按评分排序
        # 根据位置定位 省份
        hot = View.objects.filter(city=u'桂林').order_by('view_rate')[:7]

        # 随机推荐
        rand = View.objects.filter(city=u'桂林').order_by('view_rate')[::-1]

        # 猜你喜欢
        guess = View.objects.filter(city__in=[u'桂林', u'南宁'])

        data = {
            'hot': hot,
            'rand': rand,
            'guess': guess
        }

        return render(request, 'index.html', data)


@csrf_exempt
def detail(request):
    if request.method == 'GET':
        view_id = request.GET.get('id', False)
        view = View.objects.filter(id=view_id).first()

        # 类似推荐
        sim = View.objects.filter(city__in=[u'桂林', u'南宁'])

        comments = Comment.objects.filter(view=view).order_by('comment_date')[::-1]

        return render(request, 'detail.html', {'view': view, 'sim':sim, 'comments':comments})

    elif request.method == 'POST':
        comment = request.POST.get('text', False)
        view_id = request.POST.get('id', False)

        view = View.objects.get(id=view_id)
        msg = {
            'msg': u'发生未知错误',
            'type': 'danger'
        }
        if comment:
            Comment.objects.create(user=request.user, view=view, comment=comment)
            msg['msg'] = u'评论提交成功，页面即将刷新!'
            msg['type'] = 'success'

        return HttpResponse(json.dumps(msg), content_type='application/json')


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


def search(request):
    return render(request, 'search.html')