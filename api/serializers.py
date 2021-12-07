
from django.contrib.auth import get_user_model
from django.db.models import fields
from rest_framework import serializers
from about.models import Category, News
from staff.models import Subject, Teacher


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


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('title',)


class TeacherSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()

    class Meta:
        model = Teacher
        fields = '__all__'
