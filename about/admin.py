from django.contrib import admin

# Register your models here.

from about.models import News, Category, Specialty, Faculty

admin.site.register([News, Category, Specialty, Faculty])