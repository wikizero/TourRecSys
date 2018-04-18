# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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

