from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class TaskIT(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Описание')
    price = models.IntegerField(verbose_name='Бюджет')
    time_over = models.DateField(verbose_name='Срок окончания')
    # time_over = forms.DateField(input_formats=['%d/%m/%Y']),
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    time_update = models.DateTimeField(auto_now_add=True, null=True)
    place = models.CharField(max_length=255, verbose_name='Место выполнения')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Списки заказов от заказчиков'
        verbose_name_plural = 'Списки заказов от заказчиков'
        ordering = ['-time_update', 'title']

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['name']

class LoginUser(models.Model):
    username = models.CharField(max_length=255)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('username', kwargs={'username_id': self.pk})

class ContactCustomer(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('contact_customer', kwargs={'contact_customer_id': self.pk})
