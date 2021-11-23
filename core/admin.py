from django.contrib import admin

# Register your models here.

from core.models import Blog,  Certificate

admin.site.register([Blog, Certificate])