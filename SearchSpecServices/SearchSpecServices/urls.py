from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from SearchSpecServices import settings
from website.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='home'),
    path('about_us/', about_us, name='about_us'),
    path('registration/', RegisterUserCustomer.as_view(), name='registration'),
    path('registrationPerformer/', RegisterUserPerformer.as_view(), name='registrationPerformer'),
    path('sign_up/', LoginUser.as_view(), name='sign_up'),
    path('logout/', logout_user, name='logout'),
    path('category/<int:cat_id>/', show_category, name='category'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('add_taskIT/', add_taskIT, name='add_taskIT'),
    path('profile/', profile, name='profile'),
    # path('catalogIT/', CatalogIT.as_view(), name='catalogIT'),
    path('catalogIT/', TaskITAPIList.as_view(), name='catalogIT'),
    path('catalogIT/redact/<int:pk>/', TaskITAPIUpdate.as_view(), name='catalogIT_redact'),
    path('catalogIT/delete/<int:pk>/', TaskITAPIDestroy.as_view(), name='catalogIT_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)