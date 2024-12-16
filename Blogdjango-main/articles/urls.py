from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('welcome/', views.welcome, name='welcome'),
    path('time/', views.current_time, name='time'),
    path('greet/<str:name>/', views.greet_user, name='greet_user'),
]