from modeltranslation.translator import register, TranslationOptions
from core.models import MainPage, Mostquestions


@register(Mostquestions)
class MostquestionsTranslator(TranslationOptions):
    fields = ('title', 'description')

@register(MainPage)
class MainPageTranslator(TranslationOptions):
    fields = ('name', 'slogan', 'description',)