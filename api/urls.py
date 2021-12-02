from django.urls import path, include
from rest_framework import routers
from rest_framework.settings import DEFAULTS
from . import views

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register('users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('createapiview/', views.UserCreateView.as_view(), name='createapiview'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("newsapi/", views.ApiNews.as_view( ), name="newsapi"),
    path("newsapi/<int:pk>/", views.ApiNews.as_view( ), name="newsapi_detail"),
    path("blogapi/", views.ApiBlog.as_view( ), name="bloapi"),
    path("blogapi/<int:pk>/", views.ApiBlog.as_view( ), name="blogapi_detail"),
]

