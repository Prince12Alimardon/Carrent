from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Blog, About, History, How_it_works, Our_Team, Comment, Category, Tag


# Create your views here.

def blog_page(reqs):
    blogs = Blog.objects.all().order_by('-id')
    hiw = How_it_works.objects.all()
    page_number = reqs.GET.get('page')
    p = Paginator(blogs, 1)
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    ctx = {
        'blogs': blogs,
        'hiws': hiw,
        'page_obj': page_obj
    }
    return render(reqs, 'blog.html', ctx)


def about_page(req):
    abouts = About.objects.all().order_by('-id')[:1]
    teams = Our_Team.objects.all().order_by('-id')[:6]
    history = History.objects.all().order_by('-id')[:1]
    hiw = How_it_works.objects.all()
    ctx = {
        'abouts': abouts,
        'teams': teams,
        'historyies': history,
        'hiws': hiw
    }
    return render(req, 'about.html', ctx)


def blogsingle(req, pk=None):
    obj = Blog.objects.get(id=pk)
    cat = Category.objects.all()
    tag = Tag.objects.get('tag')
    ctx = {
        'obj': obj,
        'cat': cat,
        'tag': tag
    }
    return render(req, 'single.html', ctx)