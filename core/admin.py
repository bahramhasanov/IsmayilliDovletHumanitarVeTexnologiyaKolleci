from django.contrib import admin

# Register your models here.

from core.models import Mostquestions, MainPage

admin.site.register([Mostquestions, MainPage])
