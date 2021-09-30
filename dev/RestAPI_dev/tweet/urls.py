from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_tweet, name='get_tweet'),
    path('username/', views.get_username, name='get_username'),
]
