# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class View(models.Model):
    id = models.CharField(max_length=50, primary_key=True)  # city_pinyin + '_' + view_pinyin
    area = models.CharField(max_length=20)  # 如华东
    province = models.CharField(max_length=20)  # 如福建
    city = models.CharField(max_length=20)  # 如南宁
    view_name = models.CharField(max_length=25)  # 景点名称
    view_desc = models.TextField()  # 景点描述信息
    view_rate = models.CharField(max_length=5)  # 景点打分（去哪儿网系统评分）
    advise_time = models.CharField(max_length=20)  # 建议游玩时间

    def __unicode__(self):
        return self.province + '-' + self.city + '-' + self.view_name


class ExtUser(models.Model):
    user = models.OneToOneField(User)
    number = models.IntegerField(primary_key=True)
    age = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=2, blank=True, null=True)
    address = models.CharField(max_length=30, blank=True, null=True)
    autograph = models.CharField(max_length=50, blank=True, null=True)
    greet = models.CharField(max_length=50, blank=True, null=True)
    labels = models.CharField(max_length=50, blank=True, null=True)
    register_date = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.user.username


class Comment(models.Model):
    user = models.ForeignKey(User)
    view = models.ForeignKey(View)
    comment = models.CharField(max_length=255, blank=True)
    comment_date = models.DateTimeField(blank=True, auto_now=True)

    def __unicode__(self):
        return self.user.username


class Score(models.Model):
    user = models.ForeignKey(User)
    view = models.ForeignKey(View)
    rate = models.IntegerField(default=0)
    comment_date = models.DateTimeField(blank=True, auto_now=True)

    def __unicode__(self):
        return self.user.username


class Collection(models.Model):
    user = models.ForeignKey(User)
    view = models.ForeignKey(View)
    comment_date = models.DateTimeField(blank=True, auto_now=True)

    def __unicode__(self):
        return self.user.username