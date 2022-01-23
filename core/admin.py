from django.contrib import admin

# Register your models here.

from core.models import Mostquestions


@admin.register(Mostquestions)
class MostquestionsAdmin(admin.ModelAdmin):
    exclude = ('title', 'description',)
