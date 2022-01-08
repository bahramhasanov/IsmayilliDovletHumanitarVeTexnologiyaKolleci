from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AboutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'
    verbose_name = _('About')
