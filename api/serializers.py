
from django.contrib.auth import get_user_model
from django.db.models import fields
from rest_framework import serializers
from about.models import Category, News
from core.models import Blog, BlogImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)


class NewsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = '__all__'
    
    def get_created_at(self, obj):
        return obj.created_at.strftime('%d %B %Y')
        return obj.created_at.strftime('%d %m %Y')

