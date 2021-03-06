from django.contrib import admin

# Register your models here.

from core.models import Mostquestions, MainPage


@admin.register(Mostquestions)
class MostquestionsAdmin(admin.ModelAdmin):
    exclude = ('title', 'description',)


@admin.register(MainPage)
class MainPageAdmin(admin.ModelAdmin):
    exclude = ('name', 'slogan', 'description',)
