# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 20:57
# @Author  : Sinclair
# @Email   : 1178211058@qq.com
# @File    : mydecorators.py
from django.shortcuts import render


def confirm_login(func):
    def login_wrapper(request, *args, **kwargs):
        user_id = request.session.get("user")
        if user_id:
            return func(request, *args, **kwargs)
        params = {"msg": '请登录'}
        resp = render(request, "account/login.html", {"params": params})
        # resp.set_cookie("url_dest", request.get_full_path())
        referer = request.META['HTTP_REFERER']
        resp.set_cookie("url_dest", referer)
        return resp

    return login_wrapper
