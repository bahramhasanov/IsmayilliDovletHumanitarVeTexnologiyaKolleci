from django.contrib import admin

# Register your models here.

from staff.models import Teacher, Subject

admin.site.register([Teacher, Subject])