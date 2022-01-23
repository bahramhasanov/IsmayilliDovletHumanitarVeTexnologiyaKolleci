from modeltranslation.translator import register, TranslationOptions
from about.models import Category, Event, Faculty, News, Specialty, Testimonial


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


@register(Event)
class EventTranslator(TranslationOptions):
    fields = ('title', 'description')


@register(Testimonial)
class TestimonialTranslator(TranslationOptions):
    fields = ('name', 'description')
