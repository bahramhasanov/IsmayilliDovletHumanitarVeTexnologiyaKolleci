from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from about.models import News
from api.serializers import NewsSerializer

User = get_user_model()


class NewsAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)
