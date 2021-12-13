from django.db import models
from ckeditor.fields import RichTextField

from kollec.utils.base_models import BaseModel
from django.utils.translation import ugettext_lazy as _


class Mostquestions(BaseModel):
    title = models.CharField(max_length=100, verbose_name=_('Sual'))
    description = RichTextField(
        verbose_name=_("Cavab"), blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Sual')
        verbose_name_plural = _('Suallar')
