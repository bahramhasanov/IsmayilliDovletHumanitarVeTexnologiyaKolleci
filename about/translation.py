from modeltranslation.translator import register, TranslationOptions
from about.models import Category, Faculty, News, Specialty


@register(News)
class NewsTranslator(TranslationOptions):
    fields = ('title', 'description')


@register(Category)
class CategoryTranslator(TranslationOptions):
    fields = ('title',)


@register(Faculty)
class FacultyTranslator(TranslationOptions):
    fields = ('title', 'description')


@register(Specialty)
class SpecialtyTranslator(TranslationOptions):
    fields = ('title', 'description')
