from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import viewsets, permissions, status, views
from rest_framework import permissions, serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView

from api.serializers import BlogSerializer, NewsSerializer, NewsSerializer, UserSerializer
from about.models import News
from core.models import Blog

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializers_class = UserSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ApiNews(APIView):
    serializer_class = NewsSerializer
    permission_classes = (IsAdminUser,)
    
    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            obj = News.objects.get(pk=kwargs.get('pk'))
            serializer = self.serializer_class(obj, context={'request':request})
        else:
            qs = News.objects.all()
            serializer = self.serializer_class(qs, many=True, context={'request':request})
        return Response(serializer.data)

            
     
    
    
class ApiBlog(APIView):
    serializer_class = BlogSerializer
    permission_classes = (IsAdminUser,)
    
    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            obj = Blog.objects.get(pk=kwargs.get('pk'))
            serializer = self.serializer_class(obj, context={'request':request})
        else:
            qs = Blog.objects.all()
            serializer = self.serializer_class(qs, many=True, context={'request':request})
        return Response(serializer.data)
    
    
    
