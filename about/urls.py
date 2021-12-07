from django.urls import path
from . import views

urlpatterns = [
    path("news/<int:pk>", views.SingleNews.as_view(), name="news"),
    path("news/", views.AllNews.as_view(), name="allnews"),
]
