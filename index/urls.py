# _*_coding:UTF-8 _*_
from django.urls import path
from index import views

app_name = "index"

urlpatterns = [
    path("index/", views.index, name="index"),
]
