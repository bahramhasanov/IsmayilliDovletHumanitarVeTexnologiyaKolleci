from django.contrib import admin
# Register your models here.
from django.utils.html import format_html

from staff.models import Deputy, DeputyCategory, Director, Library, ReceptionDaysOfDirector, Teacher, Subject, PDF, LibraryFAQ


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    exclude = ('full_name', 'description')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    exclude = ('title',)


@admin.register(PDF)
class PDFAdmin(admin.ModelAdmin):
    exclude = ('title',)
    readonly_fields = ('slug',)

@admin.register(LibraryFAQ)
class LibraryFAQAdmin(admin.ModelAdmin):
    exclude = ('question', 'answer')

class ReceptionDaysOfDirectorInline(admin.TabularInline):
    model = ReceptionDaysOfDirector

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    exclude = ('full_name', 'description')
    inlines = [
        ReceptionDaysOfDirectorInline,
    ]

@admin.register(Deputy)
class DeputyAdmin(admin.ModelAdmin):
    exclude = ('full_name', 'description')

@admin.register(DeputyCategory)
class DeputyCategoryAdmin(admin.ModelAdmin):
    exclude = ('title',)

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    exclude = ('title', 'description')