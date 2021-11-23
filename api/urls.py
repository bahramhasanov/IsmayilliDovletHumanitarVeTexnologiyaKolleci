from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("newsapi/", views.ApiNews.as_view( ), name="newsapi"),
    path("blogapi/", views.ApiBlog.as_view( ), name="bloapi"),
    
]

