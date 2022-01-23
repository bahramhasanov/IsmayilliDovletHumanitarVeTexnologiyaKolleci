from modeltranslation.translator import register, TranslationOptions
from core.models import Mostquestions


@register(Mostquestions)
class MostquestionsTranslator(TranslationOptions):
    fields = ('title', 'description')
