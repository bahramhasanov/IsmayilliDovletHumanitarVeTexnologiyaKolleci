from django.urls import path
from . import views

urlpatterns = [
    path('teachers/', views.TeacherListView.as_view(), name='teachers'),
    # path('teachers/<int:pk>', views.TeacherListView.as_view(), name='teacher'),
]

