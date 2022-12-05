from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views


urlpatterns = [
    path('postComment', views.postComment, name="postComment"),
    
    path('', views.blogpage, name="blogpage"),
    path('<str:slug>', views.blogPost, name="blogPost")
]