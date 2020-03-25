from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from user.forms import UserModelForm

# Create your views here.
from user.models import User
from blog.models import Blog
from utils.mydecorators import confirm_login


def index(request):
    ret = Blog.objects.all().order_by('-b_create_time')
    paginator = Paginator(ret, 4)
    page_num = request.GET.get("page", 1)
    items = paginator.get_page(page_num)

    return render(request, 'index.html', {"items": items})


def register(request):
    if request.method == "GET":
        return render(request, 'account/register.html')
    form = UserModelForm(request.POST)
    form.is_valid()
    user = form.instance
    user.save()
    return render(request, 'account/login.html')


def login(request):
    if request.method == "GET":
        return render(request, 'account/login.html')
    params = request.POST.dict()
    u_tel = params['u_tel']
    u_pwd = params['u_pwd']
    user = User.objects.filter(u_tel=u_tel, u_pwd=u_pwd)
    if user:
        print(user[0].id)
        request.session['user'] = user[0].id
        url_dest = request.COOKIES.get("url_dest")
        if url_dest:
            resp = redirect(url_dest)
            resp.delete_cookie("url_dest")
        else:
            resp = redirect("/")
        return resp
    else:
        params['msg'] = "用户名或密码不正确"
        return render(request, 'account/login.html', {"params": params})


@confirm_login
def myblog(request):
    u_id = request.session['user']
    ret = Blog.objects.filter(u_id=u_id).all().order_by('-b_create_time')
    paginator = Paginator(ret, 4)
    page_num = request.GET.get("page", 1)
    items = paginator.get_page(page_num)

    return render(request, 'index.html', {"items": items})
