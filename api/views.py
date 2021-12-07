from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from about.models import Category, News
from api.serializers import NewsSerializer

User = get_user_model()


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
