
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from django.db.models import Q
from about.models import Category, Gallery, News, Faculty, Specialty, Event, Category
from api.serializers import GallerySerializer, NewsSerializer, SpecialtySerializer, TeacherSerializer, FacultySerializer
from api.serializers import EventSerializer, NewsSerializer, PDFserializer, SubjectSerializer, SubscriberSerializer, TeacherSerializer
from datetime import datetime
from django.utils.translation import get_language
from staff.models import PDF, Subject, Teacher


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
        events = Event.objects.filter(date__gte=datetime.now()) # burada datetime = qoymusan boyukdur olmamalidir ki ?!
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


class SubscriberAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GalleryAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        start = int(request.GET.get('start'))
        end = int(request.GET.get('end'))
        gallery = Gallery.objects.all()
        serializer = GallerySerializer(gallery[start:end], many=True)
        return Response(serializer.data)

    # def get(self, request):
    #     start = int(request.GET.get('start'))
    #     end = int(request.GET.get('end'))
    #     search = request.GET.get('search')
    #     lang = get_language()
    #     if search != 'all':
    #         if lang == 'ru':
    #             gallery = Gallery.objects.filter(name_ru__icontains=search)
    #         elif lang == 'en':
    #             gallery = Gallery.objects.filter(name_en__icontains=search)
    #         elif lang == 'az':
    #             gallery = Gallery.objects.filter(name_az__icontains=search)
    #     else:
    #         gallery = Gallery.objects.all()
    #     serializer = GallerySerializer(gallery[start:end], many=True)
    #     return Response(serializer.data)
