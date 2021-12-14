from django.contrib import admin

# Register your models here.

from core.models import Mostquestions, Subscrib

admin.site.register([Mostquestions, Subscrib])
