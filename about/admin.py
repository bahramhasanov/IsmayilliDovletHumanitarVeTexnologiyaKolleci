from django.contrib import admin

# Register your models here.

from about.models import News, Category

admin.site.register([News, Category])