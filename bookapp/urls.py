from django.contrib import admin
from django.urls import path,include
from .views import create_book,list_all_book,delete_book,update_book,registration,django_login,django_logout
urlpatterns=[
    path("create",create_book,name="create"),
    path("list",list_all_book,name="listbook"),
    path("delete/<int:id>",delete_book,name="delete"),
    path("update/<int:id>",update_book,name="update"),
    path("register",registration,name="register"),
    path("login",django_login,name="loginview"),
    path("logout",django_logout,name="logout")
]