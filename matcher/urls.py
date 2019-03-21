from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='matcher-home'),
    path('info/', views.info, name='matcher-info'),
]
