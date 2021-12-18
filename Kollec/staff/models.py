from django.db import models
from ckeditor.fields import RichTextField
from kollec.utils.base_models import BaseModel
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Teacher(BaseModel):
    full_name = models.CharField(
        verbose_name=_('Full Name'), max_length=50, default="")
    description = RichTextField(
        verbose_name=_("Description"), blank=True, null=True)
    photo = models.ImageField(upload_to='teachers',
                              default='teachers/default.png', verbose_name=_('Photo'))
    subject = models.ForeignKey(
        'Subject', on_delete=models.CASCADE, related_name='subject_teachers', default=1, verbose_name=_('Subject'))

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('Müəllim')
        verbose_name_plural = _('Müəllimlər')


class Subject(BaseModel):
    title = models.CharField(max_length=50, verbose_name=_('Title'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Fənn')
        verbose_name_plural = _('Fənnlər')


class PDF(BaseModel):
    title = models.CharField(
        max_length=50, verbose_name=_('Title'), help_text="Max 50 char.")
    category = models.ForeignKey(
        'staff.Subject', on_delete=models.CASCADE, related_name="pdf_category", default=None, verbose_name=_('Category'))
    file = models.FileField(upload_to='pdf/', default=None, verbose_name=_('File'))

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = _("PDF")
        verbose_name_plural = _("PDFs")
