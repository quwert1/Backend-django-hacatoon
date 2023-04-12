from django.contrib import admin

from .models import *


class TaskITAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'time_update')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('time_create', 'time_update')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

# class ChooseRoleAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     list_display_links = ('id', 'name')
#     search_fields = ('name',)
# admin.site.register(ChooseRole, ChooseRoleAdmin)

admin.site.register(TaskIT, TaskITAdmin)
admin.site.register(Category, CategoryAdmin)


