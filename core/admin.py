from django.contrib import admin

# Register your models here.

from core.models import Blog,  Certificate, BlogImage

admin.site.register([Blog, BlogImage, Certificate])