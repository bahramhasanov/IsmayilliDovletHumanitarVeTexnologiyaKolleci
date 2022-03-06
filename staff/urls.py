from django.urls import path
from . import views

urlpatterns = [
    path("director/", views.DirectorView.as_view(), name="director"),
    path("deputies/", views.DeputiesView.as_view(), name="deputies"), 
    path("departments/", views.DepartmentsView.as_view(), name="departments"),
    path('teachers/', views.TeacherListView.as_view(), name='teachers'),
    # path('teachers/<int:pk>', views.TeacherListView.as_view(), name='teacher'),
    path('library/', views.LibraryListView.as_view(), name='library'),
    path('library/<slug:slug>/<str:status>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('library/<slug:slug>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('libraryinfo/', views.LibraryInfoView.as_view(), name='libraryinfo'),
]