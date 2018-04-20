# coding:utf-8
"""TourRecSys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from tour import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # 首页
    url(r'^$', views.init),

    # 详情
    url(r'^detail', views.detail),

    # login & register & logout
    url(r'^login', views.sign_in),
    url(r'^register', views.register),
    url(r'^logout', views.sign_out),

    # 搜索
    url(r'^search', views.search),

    # 收藏
    url(r'^collection', views.collection),
]
