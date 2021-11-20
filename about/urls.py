from django.urls import path
from . import views

urlpatterns = [
    path("search/", views.news, name="news"), 
    path("fetchnews/", views.fetch_news, name="fetch_news"),
    
]