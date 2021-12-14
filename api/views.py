from datetime import datetime
from django.utils.translation import get_language
from staff.models import PDF, Subject, Teacher
from api.serializers import EventSerializer, NewsSerializer, PDFserializer, SubjectSerializer, TeacherSerializer
from about.models import Category, Event, News
from staff.models import Teacher
from api.serializers import NewsSerializer, SpecialtySerializer, TeacherSerializer, FacultySerializer
from about.models import Category, News, Faculty, Specialty
from django.db.models import Q

from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView


class NewsAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        start = int(request.GET.get('start'))
        end = int(request.GET.get('end'))
        category = request.GET.get('category')
        lang = get_language()
        if Category.objects.filter(title_en=category).exists() or Category.objects.filter(title_ru=category).exists() or Category.objects.filter(title_az=category).exists():
            if lang == 'en':
                news = News.objects.filter(
                    category=Category.objects.get(title_en=category))
            elif lang == 'ru':
                news = News.objects.filter(
                    category=Category.objects.get(title_ru=category))
            elif lang == 'az':
                news = News.objects.filter(
                    category=Category.objects.get(title_az=category))
        else:
            news = News.objects.all()
        serializer = NewsSerializer(news[start:end], many=True)
        return Response(serializer.data)


class TeacherAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        start = int(request.GET.get('start'))
        end = int(request.GET.get('end'))
        search = request.GET.get('search')
        lang = get_language()
        if search != 'all':
            if lang == 'ru':
                teachers = Teacher.objects.filter(
                    Q(full_name_ru__icontains=search) | Q(subject__title_ru__icontains=search))
            elif lang == 'en':
                teachers = Teacher.objects.filter(
                    Q(full_name_en__icontains=search) | Q(subject__title_en__icontains=search))
            elif lang == 'az':
                teachers = Teacher.objects.filter(
                    Q(full_name_az__icontains=search) | Q(subject__title_az__icontains=search))
        else:
            teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers[start:end], many=True)
        return Response(serializer.data)


class FacultyAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        faculties = Faculty.objects.all()
        serializer = FacultySerializer(faculties, many=True)
        return Response(serializer.data)


class FacultyDetailAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, pk):
        faculty = Faculty.objects.get(id=pk)
        serializer = FacultySerializer(faculty)
        return Response(serializer.data)


class SpecialityAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        faculties = Specialty.objects.all()
        serializer = SpecialtySerializer(faculties, many=True)
        return Response(serializer.data)


class SpecialityDetailAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, pk2):
        faculty = Specialty.objects.get(id=pk2)
        serializer = SpecialtySerializer(faculty)
        return Response(serializer.data)


class PDFAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        start = int(request.GET.get('start'))
        end = int(request.GET.get('end'))
        category = request.GET.get('category')
        lang = get_language()
        if Subject.objects.filter(title_en=category).exists() or Subject.objects.filter(title_ru=category).exists() or Subject.objects.filter(title_az=category).exists():
            if lang == 'en':
                pdf = PDF.objects.filter(
                    category__title_en__icontains=category)
            elif lang == 'ru':
                pdf = PDF.objects.filter(
                    category__title_ru__icontains=category)
            elif lang == 'az':
                pdf = PDF.objects.filter(
                    category__title_az__icontains=category)
        else:
            pdf = PDF.objects.all()
        serializer = PDFserializer(pdf[start:end], many=True)
        return Response(serializer.data)


class SubjectAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        subject = request.GET.get('subject')
        lang = get_language()
        if subject:
            if lang == 'en':
                subjects = Subject.objects.filter(
                    title_en__icontains=subject)
            elif lang == 'ru':
                subjects = Subject.objects.filter(
                    title_ru__icontains=subject)
            elif lang == 'az':
                subjects = Subject.objects.filter(
                    title_az__icontains=subject)
        else:
            subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)


class FutureEventAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        events = Event.objects.filter(date__gte=datetime.now())
        serializer = EventSerializer(events[2:], many=True)
        return Response(serializer.data)


class RecentEventAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        start = int(request.GET.get('start'))
        end = int(request.GET.get('end'))
        events = Event.objects.filter(date__lte=datetime.now())
        serializer = EventSerializer(events[start:end], many=True)
        return Response(serializer.data)
