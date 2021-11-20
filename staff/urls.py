from django.urls import path
from . import views

urlpatterns = [
    # path("teacher/", views.teacher.as_view(), name="teacher"), 
    path("teacher/", views.teacher, name="teacher"), 
    
    # path('product-list/', views.ProductListView.as_view(), name="product_list"),
]

