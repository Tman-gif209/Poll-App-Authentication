from django.urls import path
from .import views
from .models import Post
from django.views.generic import ListView
from django.contrib.auth import views as auth_views

from user_auth import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from polls.views import index

app_name = 'user_auth'
urlpatterns = [
    path('', views.home, name='home'),
    #path('home/', views.home, name='home'),
    path('login.html/', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('register.html', user_views.register, name='register'),
    path('user.html', views.show_user, name='show_user'),
    path('poll.html', index, name='index'),
    
]
