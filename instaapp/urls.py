from django.urls import path,re_path
from django.contrib import admin
from .import views
from . import views as app_views


urlpatterns = [
    path('',views.index,name = 'index'),
    path('',views.welcome,name = 'welcome'),
    path('profile/', views.profile, name='profile'),
    path('like/', views.like_image, name='like-image'),
    # path('<slug:slug>/', views.photo_detail, name='photo_detail'),
    path('search/', views.search, name='search'),
    
]