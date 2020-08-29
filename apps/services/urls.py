from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('services', views.Services, name='services')
]