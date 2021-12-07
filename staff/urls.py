from django.urls import path
from . import views

urlpatterns = [
    path("deputies/", views.Deputies.as_view(), name="deputies"), 
    path("director/", views.Director.as_view(), name="director"),
    path('teachers/', views.TeacherListView.as_view(), name='teachers'),
    # path('teachers/<int:pk>', views.TeacherListView.as_view(), name='teacher'),
]

