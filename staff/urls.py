from django.urls import path
from . import views

urlpatterns = [
    path("director/", views.Director.as_view(), name="director"),
    path("deputies/", views.Deputies.as_view(), name="deputies"), 
    path("departments/", views.Departments.as_view(), name="departments"),
    path('teachers/', views.TeacherListView.as_view(), name='teachers'),
    # path('teachers/<int:pk>', views.TeacherListView.as_view(), name='teacher'),
]

