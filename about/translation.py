from modeltranslation.translator import register, TranslationOptions
from about.models import About, Category, Contact, Event, FBKTeacher, Faculty, News, Specialty, Testimonial

@register(FBKTeacher)
class FBKTeacherTranslationOptions(TranslationOptions):
    fields = ('full_name',)


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

@register(Contact)
class ContactTranslator(TranslationOptions):
    fields = ('title', 'address')

@register(About)
class AboutTranslator(TranslationOptions):
    fields = ('title', 'description')
