from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.contrib.auth import logout, login
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.viewsets import GenericViewSet
from rest_framework import generics, viewsets, mixins

from .models import *
from .forms import *
from .utils import *
from .serializers import *
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


def main_page(request):
    return render(request, 'website/index.html', {'title': 'Главная страница'})

def about_us(request):
    return render(request, 'website/about_us.html', {'title': 'О нас'})


class RegisterUserCustomer(DataMixin, CreateView):
    role = 'Заказчик'
    form_class = RegisterUserCustomerForm
    template_name = 'website/registration.html'
    success_url = reverse_lazy('sign_up')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация - заказчик")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('catalogIT')

class RegisterUserPerformer(DataMixin, CreateView):
    role = 'Заказчик'
    form_class = RegisterUserPerformerForm
    template_name = 'website/registrationPerformer.html'
    success_url = reverse_lazy('sign_up')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация - исполнитель")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('catalogIT')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'website/sign_up.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('profile')

def profile(request):
    return render(request, 'website/profile.html', {'title': 'Профиль'})

def logout_user(request):
    logout(request)
    return redirect('home')


# class CatalogIT(ListView):
#     model = TaskIT
#     template_name = 'website/catalogIT.html'
#     context_object_name = 'posts'
#     paginate_by = 15
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Каталог заказов IT'
#         context['cats'] = Category.objects.all()
#         context['cat_selected'] = 0
#         return context


# class CatalogAPIList(generic.ListCreateAPIView):
#     queryset = TaskIT.objects.all()
#
#
# class CatalogAPIUpdate(generic.RetrieveUpdateAPIView):




class TaskITAPIList(generics.ListCreateAPIView):
    queryset = TaskIT.objects.all()
    serializer_class = TaskITSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class TaskITAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = TaskIT.objects.all()
    serializer_class = TaskITSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class TaskITAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = TaskIT.objects.all()
    serializer_class = TaskITSerializer
    permission_classes = (IsAdminOrReadOnly, )







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
        'category_selected': post.category_id,
    }
    return render(request, 'website/post.html', context=context)


def add_taskIT (request):
    if request.method == 'POST':
        form = AddTaskIT_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogIT')
    else:
        form = AddTaskIT_Form()
    return render(request, 'website/add_taskIT.html', {'title': 'Add article', 'form': form})