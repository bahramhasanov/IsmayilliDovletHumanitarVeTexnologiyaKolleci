from django.urls import path
from . import views

urlpatterns = [
    path("base/", views.Base.as_view(), name="base"), 
]