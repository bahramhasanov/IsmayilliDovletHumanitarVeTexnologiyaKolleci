import datetime
from django.db import models
from ckeditor.fields import RichTextField
from kollec.utils.base_models import BaseModel
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from pytz import timezone
# Create your models here.

class Department(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    slug = models.SlugField(max_length=255, unique=True, verbose_name=_('Slug'), blank=True, null=True)
    description = RichTextField(verbose_name=_('Description'))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Department, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')


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
    file = models.FileField(
        upload_to='pdf/', default=None, verbose_name=_('File'))
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            now = datetime.datetime.now(timezone('Asia/Baku'))
            self.slug = slugify(f"{self.title}-{now}")
        super(PDF, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("PDF")
        verbose_name_plural = _("PDFs")


class Library(BaseModel):
    title = models.CharField(
        max_length=50, verbose_name=_('Title'), help_text="Max 50 char.")
    description = RichTextField(
        verbose_name=_("Description"))

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = _("Library")
        verbose_name_plural = _("Libraries")


class LibraryFAQ(BaseModel):
    question = models.CharField(max_length=50, verbose_name=_('Question'))
    answer = RichTextField(verbose_name=_('Answer'))

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = _('Library FAQ')
        verbose_name_plural = _('Library FAQs')


class Director(BaseModel):
    full_name = models.CharField(
        verbose_name=_('Full Name'), max_length=50, default="")
    image = models.ImageField(upload_to='director/',
                              default=None, verbose_name=_('Image'))
    description = RichTextField(
        verbose_name=_("Description"), blank=True, null=True)
    email = models.EmailField(
        verbose_name=_('Email'), max_length=50, default="")
    start_date = models.DateField(
        verbose_name=_('Start Date'), default=None, null=True)
    end_date = models.DateField(
        verbose_name=_('End Date'), default=None, null=True)

    def __str__(self) -> str:
        return f"{self.full_name}"

    class Meta:
        verbose_name = _("Director")
        verbose_name_plural = _("Directors")


class ReceptionDaysOfDirector(BaseModel):
    start_time = models.TimeField(
        verbose_name=_('Start Time'), default=None, null=True)
    end_time = models.TimeField(
        verbose_name=_('End Time'), default=None, null=True)
    director = models.ForeignKey(
        'staff.Director', on_delete=models.CASCADE, related_name='director_days', default=None, verbose_name=_('Director'))

    def __str__(self) -> str:
        return f"{self.director}"

    class Meta:
        verbose_name = _("Reception Days Of Director")
        verbose_name_plural = _("Reception Days Of Directors")


class Deputy(BaseModel):
    full_name = models.CharField(
        verbose_name=_('Full Name'), max_length=50, default="")
    image = models.ImageField(upload_to='deputy/',
                              default=None, verbose_name=_('Image'))
    description = RichTextField(
        verbose_name=_("Description"), blank=True, null=True)
    phone = models.CharField(
        verbose_name=_('Phone'), max_length=50, default="")
    category = models.ForeignKey(
        'staff.DeputyCategory', on_delete=models.CASCADE, related_name='deputy_category', default=None, verbose_name=_('Category'))

    def __str__(self) -> str:
        return f"{self.full_name}"

    class Meta:
        verbose_name = _("Deputy")
        verbose_name_plural = _("Deputies")


class DeputyCategory(BaseModel):
    title = models.CharField(max_length=50, verbose_name=_('Title'))

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = _("Deputy Category")
        verbose_name_plural = _("Deputy Categories")


class HeadOfDepartment(BaseModel):
    department = models.ForeignKey(
        'staff.Department', on_delete=models.CASCADE, related_name='head_of_department', default=None, verbose_name=_('Department'))
    full_name = models.CharField(
        verbose_name=_('Full Name'), max_length=70, default="")
    description = RichTextField(
        verbose_name=_("Description"), blank=True, null=True)
    phone = models.CharField(
        verbose_name=_('Phone'), max_length=50, default="")
    image = models.ImageField(upload_to='department/',
                                default=None, verbose_name=_('Image'))
    
    def __str__(self) -> str:
        return f"{self.full_name}"

    class  Meta:
        verbose_name = _("Head Of Department")
        verbose_name_plural = _("Head Of Departments")
    