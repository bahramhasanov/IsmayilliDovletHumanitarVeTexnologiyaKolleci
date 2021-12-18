from django.urls import path, include
from rest_framework import routers
from rest_framework.settings import DEFAULTS
from . import views

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('newsapi/', views.NewsAPIView.as_view(), name='newsapi'),
    path('futureeventapi/', views.FutureEventAPIView.as_view(),
         name='futureeventapi'),
    path('recenteventapi/', views.RecentEventAPIView.as_view(),
         name='recenteventapi'),
    path('teacherapi/', views.TeacherAPIView.as_view(), name='teacherapi'),
    path('facultyapi/', views.FacultyAPIView.as_view(), name='facultyapi'),
    path('facultyapi/<int:pk>/',
         views.FacultyDetailAPIView.as_view(), name='faculty_detail'),
    path('specialityapi/', views.SpecialityAPIView.as_view(), name='specialityapi'),
    path('specialityapi/<int:pk>/',
         views.SpecialityDetailAPIView.as_view(), name='speciality_detail'),
    path('pdfapi/', views.PDFAPIView.as_view(), name='pdfapi'),
    path('subjectapi/', views.SubjectAPIView.as_view(), name='subjectapi'),
    path('subscriberapi/', views.SubscriberAPIView.as_view(), name='subscriberapi'),
]
