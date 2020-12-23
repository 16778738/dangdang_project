# _*_coding:UTF-8 _*_
from django.urls import path

from book import views

app_name = "book"
urlpatterns = [
    path('booklist/', views.booklist,name="booklist"),
    path('bookdetails/', views.bookdetails,name="bookdetails"),

]
