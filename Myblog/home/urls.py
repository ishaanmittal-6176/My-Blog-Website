from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("search", views.search, name="search"),
    path("signin", views.signin, name="signin"),
    path("blogLogin", views.blogLogin , name="blogLogin"),
    path("blogLogout", views.blogLogout , name="blogLogout"),
]