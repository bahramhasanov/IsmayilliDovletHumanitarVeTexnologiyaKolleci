import datetime
from django.utils.translation import get_language


def get_language_info(request):
    context = {
        'lang': get_language(),
        'lang_name': request.LANGUAGE_CODE,
        'year': datetime.datetime.now().year,
    }
    return context
