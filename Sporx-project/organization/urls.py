from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('login_success', views.login_succes, name='login_success')
]
