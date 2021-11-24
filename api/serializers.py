
from django.contrib.auth import get_user_model
from django.db.models import fields
from rest_framework import serializers
from about.models import News, NewsImage
from core.models import Blog, BlogImage

User = get_user_model()


class NewsImagesSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    
    class Meta:
        model = NewsImage
        fields = ('id',
                  'name',
                  'url',
            )
    
    def get_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.image.url)
  
  
class NewsSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    class Meta:
        model = News
        fields = ('id',
                  'name',
                  'subtitle',
                  'description',
                  'images',
            )
        
    def get_images(self, obj):
        request = self.context.get('request')
        return NewsImagesSerializer(obj.images.all(), many=True, context={'request':request}).data


class BlogImagesSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    
    class Meta:
        model = BlogImage
        fields = ('id',
                  'url',
            )
    
    def get_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.image.url)
    
    
class BlogSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    class Meta:
        model = Blog
        fields = ('id',
                  'title',
                  'subtitle',
                  'description',
                  'images',)
    
    def get_images(self, obj):
        request = self.context.get('request')
        return BlogImagesSerializer(obj.images.all(), many=True, context={'request':request}).data
        
