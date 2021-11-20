from django.contrib import admin

# Register your models here.

from about.models import Subject, Topic, News, NewsImage

admin.site.register([Subject, Topic, News, NewsImage])