from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings

from .views import home ,post , category , aboutus , contact , create_account , postComment ,contact_us_form

from . import views

from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='home/')),
    path('home/', home),
    path('blog/<slug:url>',post),
    path('category/<slug:url>',category),
    path('aboutus/',aboutus),
    path('contact/',contact),

    path('creataccount/', views.create_account, name='new_user'), # was not working with slash now suddenly working ?
    path('login/', views.user_login, name='login_user'),
    path('logout/', views.user_logout, name='log_out'),

    path('postComment', views.postComment, name="postComment"),
    path('formMessage',views.contact_us_form,name="formMessage")
]
