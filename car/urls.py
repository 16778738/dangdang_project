# _*_coding:UTF-8 _*_
from django.urls import path
from car import views

app_name = 'car'
urlpatterns = [
    path('car/', views.car, name='car'),
    path('add_car/', views.add_car, name='add_car'),
    path('rem_book/', views.rem_book, name='rem_book'),
    path('order/', views.order, name='order'),
    path('order_ok/', views.order_ok, name='order_ok'),
    path('order_submit/', views.order_submit, name='order_submit'),
]
