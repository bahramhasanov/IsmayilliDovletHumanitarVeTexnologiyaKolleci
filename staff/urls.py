from django.urls import path
from . import views

urlpatterns = [
    # path("teacher/", views.teacher.as_view(), name="teacher"), 
    path("teacher/", views.teacher, name="teacher"), 
    path("deputies/", views.Deputies.as_view(), name="deputies"), 
    path("director/", views.Director.as_view(), name="director"),
    # path('product-list/', views.ProductListView.as_view(), name="product_list"), 
]

