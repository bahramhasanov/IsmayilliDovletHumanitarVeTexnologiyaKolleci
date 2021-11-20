from django.shortcuts import render


from about.models import News


from django.contrib.auth import get_user_model

from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from api.serializers import NewsSerializer

from api.serializers import NewsSerializer

User = get_user_model()

class ApiNews(APIView):
    serializer_class = NewsSerializer
    permission_classes = (IsAdminUser,)
    
    def get(self, request, format=None):
        qs = News.objects.all()
        serializer = NewsSerializer(qs, many=True)
        return Response(serializer.data)

    
    
    
