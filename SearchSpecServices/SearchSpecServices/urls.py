from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from SearchSpecServices import settings
from website.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='home'),
    path('about_us/', about_us, name='about_us'),
    path('registration/', regist, name='registration'),
    # path('registration/', RegisterUser.as_view(), name='registration'),
    path('sign_up/', sign_up, name='sign_up'),
    # path('catalogIT/', CatalogIT.as_view(), name='catalogIT'),
    path('catalogIT/', catalog, name='catalogIT'),
    path('category/<int:cat_id>/', show_category, name='category'),
    path('post/<int:post_id>/', show_post, name='post')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)