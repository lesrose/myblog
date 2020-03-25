# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 17:21
# @Author  : Sinclair
# @Email   : 1178211058@qq.com
# @File    : forms.py
from django.forms import ModelForm
from user.models import User


class UserModelForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"
