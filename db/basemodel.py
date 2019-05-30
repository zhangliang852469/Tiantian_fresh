#!/usr/bin/env python3
# encoding: utf-8

from django.db import models



class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='删除')

    class Meta:
        """抽象基类，所有模型都存在，用于继承"""
        abstract = True







