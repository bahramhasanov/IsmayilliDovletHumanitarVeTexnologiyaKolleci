from django.db.models import Q

from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.views import APIView
from about.models import Category, News, Faculty, Specialty
from api.serializers import NewsSerializer, SpecialtySerializer, TeacherSerializer, FacultySerializer
from staff.models import Teacher


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


class SpecialtyAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        faculties = Specialty.objects.all()
        serializer = SpecialtySerializer(faculties, many=True)
        return Response(serializer.data)

# class FacultyAPIView(APIView):
#     serializer_class = FacultySerializer

#     def get(self, request, *args, **kwargs):
#         if kwargs.get("pk"):
#             obj = Faculty.objects.get(pk=kwargs.get("pk"))
#             serializer = self.serializer_class(obj)
#         else:
#             obj = Faculty.objects.all()
#             serializer = self.serializer_class(obj, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)