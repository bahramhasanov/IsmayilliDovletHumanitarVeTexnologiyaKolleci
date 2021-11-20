from django.contrib import admin

# Register your models here.

from staff.models import Teacher, FBK,Department, Student, Group

admin.site.register([Teacher, FBK, Department,Student, Group])