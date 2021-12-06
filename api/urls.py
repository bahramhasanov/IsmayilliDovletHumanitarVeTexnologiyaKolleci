from django.urls import path, include
from rest_framework import routers
from rest_framework.settings import DEFAULTS
from . import views

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('newsapi/', views.NewsAPIView.as_view(), name='newsapi'),
]
