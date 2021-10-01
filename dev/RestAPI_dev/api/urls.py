from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
from .views import *


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('tweet', views.TweetCreateAPI)
# router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('tweets/', TweetsListAPI.as_view()),
    path('tweet/<username>/', TweetUsernameAPI.as_view()),
]
