
from staff.models import PDF, Subject, Teacher
from about.models import Category, News
from staff.models import Subject, Teacher
from about.models import Category, News, Specialty, Faculty
from django.contrib.auth import get_user_model
from rest_framework import serializers

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


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'


class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'


class PDFserializer(serializers.ModelSerializer):
    category = SubjectSerializer()
    size = serializers.SerializerMethodField()

    class Meta:
        model = PDF
        fields = '__all__'

    def get_size(self, obj):
        return obj.file.size
