from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from .models import *


def main_page(request):
    return render(request, 'website/index.html', {'title': 'Главная страница'})

def about_us(request):
    return render(request, 'website/about_us.html', {'title': 'О нас'})

def regist(request):
    return render(request, 'website/registration.html', {'title': 'Регистрация'})

def sign_up(request):
    return render(request, 'website/sign_up', {'title': 'Вход в аккаунт'})

# class CatalogIT(ListView):
#     model = TaskIT
#     template_name = 'website/catalogIT.html'
#     posts = TaskIT.objects.all()
#     cats = Category.objects.all()
#
#     paginate_by = 15
#     context_object_name = 'posts'
#     extra_context = {'title': 'Каталог IT услуг',}
#
#     def get_queryset(self):
#         return TaskIT.objects.all()


def catalog(request):
    posts = TaskIT.objects.all()
    cats = Category.objects.all()

    context = {
        'posts': posts,
        'cats': cats,
        'title': 'Catalog',
        'cat_selected': 0,
    }
    return render(request, 'website/catalogIT.html', context=context)

def show_category(request, cat_id):
    posts = TaskIT.objects.filter(category=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'title': 'Catalog',
        'cat_selected': cat_id,
    }

    return render(request, 'website/catalogIT.html', context=context)

def show_post(request, post_id):
    post = get_object_or_404(TaskIT, pk=post_id)

    context = {
        'post': post,
        'title': post.title,
    }
    return render(request, 'website/post.html', context=context)