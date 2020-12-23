# _*_coding:UTF-8 _*_
from django.urls import path

from user import views

app_name = 'user'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('login_logic/', views.login_logic, name='login_logic'),
    path('regist/', views.regist, name='regist'),
    path('redist_logic/', views.regist_logic, name='regist_logic'),
    path('getCaptcha/', views.getCaptcha, name='getCaptcha'),
    path('regist_ok/', views.regist_ok, name='regist_ok'),
    path('check_code/', views.check_code, name='check_code'),
    path('check_username/', views.check_username, name='check_username'),
    path('exit/', views.exit, name='exit'),
]
