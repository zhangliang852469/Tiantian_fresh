from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from db.basemodel import BaseModel

"""与用户相关的有两张表： 用户和地址 """



class User(AbstractBaseUser, BaseModel):
    """用户表"""

    class Meta:
        db_table = 'df_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name




class AddressManger(models.Manager):
    """地址管理"""
    # 1. 改变原有查询的结果集:all()
    # 2. 封装方法：用户操作模型类对应的数据表
    def get_default_address(self, user):
        """默认地址"""
        try:
            address = self.model.objects.get(user=user, is_default=True)
        except self.model.DoesNotExist:
            """地址为空"""
            address = None
        return address


class Address(BaseModel):
    """地址"""
    user = models.ForeignKey('User', verbose_name='所属用户')
    receiver = models.CharField(max_length=64, verbose_name='收件人')
    re_address = models.CharField(max_length=256, verbose_name='收件地址')
    zip_code = models.CharField(max_length=6, null=True, verbose_name='邮编')
    phone = models.CharField(max_length=11, verbose_name='联系电话')
    is_default = models.BooleanField(default=False, verbose_name='是否设为默认地址')


    # 管理器
    objects = AddressManger()


    class Meta:
        db_table = 'df_address'
        verbose_name = '地址'
        verbose_name_plural = verbose_name
















