from django.contrib import admin

# Register your models here.

from staff.models import Teacher, Subject, PDF

admin.site.register([Teacher, Subject, PDF])