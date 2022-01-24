from django.db import models
from ckeditor.fields import RichTextField

from kollec.utils.base_models import BaseModel
from django.utils.translation import ugettext_lazy as _


class Mostquestions(BaseModel):
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    description = RichTextField(verbose_name=_("Cavab"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Sual')
        verbose_name_plural = _('Suallar')


class MainPage(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    slogan = models.CharField(max_length=100, verbose_name=_('Name'))
    description = RichTextField(
        verbose_name=_("description"), blank=True, null=True)
    active_student_number = models.IntegerField()
    faculty_number = models.IntegerField()
    graduate_number = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('MainPage')
        verbose_name_plural = _('MainPage')
