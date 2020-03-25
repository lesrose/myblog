# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 18:09
# @Author  : Sinclair
# @Email   : 1178211058@qq.com
# @File    : urls.py
from django.urls import path
from . import views

app_name = "notes"
urlpatterns = [
    path("mynotes", views.mynotes, name="mynotes"),
    path("add", views.add, name="add"),
    path("modify", views.modify, name="modify"),
    path("del/<str:pk>", views.delete, name="delete"),
]