
from django.contrib.auth import get_user_model
from django.db.models import fields
from rest_framework import serializers
from about.models import News
from core.models import Blog

User = get_user_model()

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
        
    def get_serializer(self,obj):
        return NewsSerializer(obj, many=True) 
        

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        
    def get_serializer(self,obj):
        return NewsSerializer(obj, many=True) # buna gerek var mi?
        

    