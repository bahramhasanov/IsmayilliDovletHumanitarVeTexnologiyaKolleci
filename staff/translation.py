from modeltranslation.translator import register, TranslationOptions
from staff.models import (
    PDF, Deputy, DeputyCategory, Director, Library, LibraryFAQ, Subject, Teacher, HeadOfDepartment, Department
)

@register(Department)
class DepartmentTranslator(TranslationOptions):
    fields = ('title', 'description')


@register(HeadOfDepartment)
class HeadOfDepartmentTranslator(TranslationOptions):
    fields = ('full_name', 'description')


@register(Teacher)
class TeacherTranslator(TranslationOptions):
    fields = ('full_name', 'description')


@register(Subject)
class SubjectTranslator(TranslationOptions):
    fields = ('title',)


@register(PDF)
class PDFTranslator(TranslationOptions):
    fields = ('title',)

@register(LibraryFAQ)
class LibraryFAQTranslator(TranslationOptions):
    fields = ('question', 'answer')

@register(Director)
class DirectorTranslator(TranslationOptions):
    fields = ('full_name', 'description')

@register(Deputy)
class DeputyTranslator(TranslationOptions):
    fields = ('full_name', 'description')

@register(DeputyCategory)
class DeputyCategoryTranslator(TranslationOptions):
    fields = ('title',)

@register(Library)
class LibraryTranslator(TranslationOptions):
    fields = ('title', 'description')