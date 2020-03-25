# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 16:35
# @Author  : Sinclair
# @Email   : 1178211058@qq.com
# @File    : urls.py
from django.urls import path
from . import views

app_name = "user"
urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("myblog", views.myblog, name="myblog"),
]