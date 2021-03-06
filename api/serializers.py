
from django.db.models import fields
from staff.models import PDF, Subject, Teacher, TeacherTextColor
from about.models import Category, Event, Gallery, News, Subscriber, Testimonial
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

class TeacherTextColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherTextColor
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    text_color = TeacherTextColorSerializer()

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


class EventSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    date = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = '__all__'

    def get_date(self, obj):
        return obj.date.strftime('%B %d, %Y %H:%M')


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        fields = '__all__'


class TestimonialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Testimonial
        fields = '__all__'
