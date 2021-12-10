from django.db.models import Q

from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from about.models import Category, News
from api.serializers import NewsSerializer, PDFserializer, TeacherSerializer
from staff.models import PDF, Subject, Teacher


class NewsAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        start = int(request.GET.get('start'))
        end = int(request.GET.get('end'))
        category = request.GET.get('category')
        if Category.objects.filter(title=category).exists():
            news = News.objects.filter(
                category=Category.objects.get(title=category))
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
        if search != 'all':
            teachers = Teacher.objects.filter(
                Q(full_name__icontains=search) | Q(subject__title__icontains=search))
        else:
            teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers[start:end], many=True)
        return Response(serializer.data)


class PDFAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        start = int(request.GET.get('start'))
        end = int(request.GET.get('end'))
        category = request.GET.get('category')
        if Subject.objects.filter(title=category).exists():
            pdf = PDF.objects.filter(
                category=Subject.objects.get(title=category))
        else:
            pdf = PDF.objects.all()
        serializer = PDFserializer(pdf[start:end], many=True)
        return Response(serializer.data)
