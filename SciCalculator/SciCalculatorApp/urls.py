from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('number_conversion/', views.number_conversion, name='number_conversion'),
    path('ip_conversion/', views.ip_conversion, name='ip_conversion'),
    #path('result/', views.result, name='result'),
]