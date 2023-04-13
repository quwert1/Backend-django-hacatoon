from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from SearchSpecServices import settings
from website.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='home'),
    path('about_us/', about_us, name='about_us'),
    path('about_us_perf/', about_us_perf, name='about_us_perf'),
    path('registration/', RegisterUserCustomer.as_view(), name='registration'),
    path('registrationPerformer/', RegisterUserPerformer.as_view(), name='registrationPerformer'),
    path('sign_up/', LoginUser.as_view(), name='sign_up'),
    path('logout/', logout_user, name='logout'),
    path('category/<int:cat_id>/', show_category, name='category'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('post/<int:post_id>/', show_post_cust, name='post_cust'),
    path('add_taskIT/', add_taskIT, name='add_taskIT'),
    path('profile/', profile, name='profile'),
    path('profile_perf/', profile_perf, name='profile_perf'),
    path('catalogIT_cust/', CatalogIT.as_view(), name='catalogIT_cust'),
    path('catalogIT_perf/', CatalogIT_perf.as_view(), name='catalogIT_perf'),
    path('catalogIT/redact/<int:pk>/', TaskITAPIUpdate.as_view(), name='catalogIT_redact'),
    path('catalogIT/delete/<int:pk>/', TaskITAPIDestroy.as_view(), name='catalogIT_delete'),
    path('who_are_you/', who_are_you, name="who_are_you"),
]

handler404 = pageNotFound

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)