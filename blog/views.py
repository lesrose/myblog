from django.shortcuts import render, redirect

# Create your views here.
from blog.models import Blog
from comment.models import Comment
from datetime import datetime
from utils.mydecorators import confirm_login


def detail(request, pk):
    blog = Blog.objects.filter(pk=pk)
    blog = blog[0]
    comments = Comment.objects.filter(b_id=pk).all()
    blog.b_read_num += 1
    blog.save()
    return render(request, 'single.html', {"blog": blog, "comments": comments})


@confirm_login
def comment(request, pk):
    u_id = request.session['user']
    com = Comment.objects.filter(u_id=u_id, b_id=pk)
    if com:
        return redirect('blog:detail', pk=pk)
    b_id = pk
    c_content = request.POST.dict()['comment']
    com = Comment(u_id=u_id, b_id=b_id, c_create_time=datetime.now(), c_content=c_content)
    com.save()
    return redirect('blog:detail', pk=pk)
    # return redirect('/')


@confirm_login
def add(request):
    if request.method == "GET":
        return render(request, 'add_blog.html')
    params = request.POST.dict()
    u_id = request.session['user']
    c_time = datetime.now()
    m_time = datetime.now()
    b_tags = params['tags']
    b_content = params['content']
    b_title = params['title']
    blog = Blog(u_id=u_id, b_create_time=c_time, b_modify_time=m_time, b_tags=b_tags, b_content=b_content,
                b_title=b_title)
    blog.save()
    return redirect('/')
