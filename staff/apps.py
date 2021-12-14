from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class StaffConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'staff'
    verbose_name = _('Staff')
