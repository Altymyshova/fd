
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path ('url1/', views.text1),
path ('url2/', views.text2),
path ('url3/', views.text3),
path ('comments/', views.commentshow)
]
