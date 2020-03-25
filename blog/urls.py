# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 18:09
# @Author  : Sinclair
# @Email   : 1178211058@qq.com
# @File    : urls.py
from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("detail/<int:pk>", views.detail, name="detail"),
    path("comment/<int:pk>", views.comment, name="comment"),
    path("add", views.add, name="add"),
]