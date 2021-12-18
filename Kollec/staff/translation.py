from modeltranslation.translator import register, TranslationOptions
from staff.models import PDF, Subject, Teacher


@register(Teacher)
class TeacherTranslator(TranslationOptions):
    fields = ('full_name', 'description')


@register(Subject)
class SubjectTranslator(TranslationOptions):
    fields = ('title',)


@register(PDF)
class PDFTranslator(TranslationOptions):
    fields = ('title',)
