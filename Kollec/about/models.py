from django.db import models
from ckeditor.fields import RichTextField

from kollec.utils.base_models import BaseModel
from django.utils.translation import ugettext_lazy as _


class News(BaseModel):
    title = models.CharField(
        max_length=30, verbose_name=_('Title'), help_text="Max 30 char.")
    # description = models.TextField(verbose_name="Description", null=True, blank=True)
    description = RichTextField(
        verbose_name=_("Description"), blank=True, null=True)
    category = models.ForeignKey(
        'about.Category', on_delete=models.CASCADE, related_name="news_category", default=None, verbose_name=_("Category"))
    image = models.ImageField(
        upload_to='news/', default=None, verbose_name=_("Image"))

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = _("Xəbər")
        verbose_name_plural = _("Xəbərlər")


class Category(BaseModel):
    title = models.CharField(
        max_length=30, verbose_name=_('Title'), help_text="Max 30 char.")

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = _("Kateqoriya")
        verbose_name_plural = _("Kateqoriyalar")


class Faculty(BaseModel):
    title = models.CharField(
        max_length=30, verbose_name=_('Title'), help_text="Max 30 char.")
    description = RichTextField(
        verbose_name=_("Description"), blank=True, null=True)
    image = models.ImageField(upload_to='faculty/',
                              default=None, verbose_name=_("Image"))
    # FBK = models.OneToOneField(Teacher, on_delete=models.CASCADE, related_name='faculty_teacher', default=1, null=True, blank=True)

    def __str__(self) -> str:
        return 'f"{self.title}"'

    class Meta:
        verbose_name = _("FBK")
        verbose_name_plural = _("FBKlar")


class Specialty(BaseModel):
    title = models.CharField(
        max_length=30, verbose_name=_('Title'), help_text="Max 30 char.")
    description = RichTextField(
        verbose_name=_("Description"), blank=True, null=True)
    image_icon = models.ImageField(
        upload_to='specialty/', default=None, verbose_name=_("Image"))
    faculty = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, related_name="specialty_faculty", default=None, verbose_name=_("Faculty"))

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = _("Ixtisas")
        verbose_name_plural = _("Ixtisaslar")


class Admissionrules(BaseModel):
    total_rules = RichTextField(
        verbose_name=_("Description"), blank=True, null=True)
    from_9_rules = RichTextField(
        verbose_name=_("Description"), blank=True, null=True)
    from_11_rules = RichTextField(
        verbose_name=_("Description"), blank=True, null=True)

    def __str__(self) -> str:
        return 'qəbul'

    class Meta:
        verbose_name = _("qəbul qaydaları")
        verbose_name_plural = _("qəbul qaydaları")


class About(BaseModel):
    description = RichTextField(
        verbose_name=_("Description"), blank=True, null=True)
    image = models.ImageField(
        upload_to='about/', default=None, verbose_name=_("Image"))

    def __str__(self) -> str:
        return 'Haqqımızda'

    class Meta:
        verbose_name = _("Haqqımızda")
        verbose_name_plural = _("Haqqımızda")


class Event(BaseModel):
    title = models.CharField(
        max_length=30, verbose_name=_('Title'), help_text="Max 30 char.")
    description = RichTextField(
        verbose_name=_("Description"))
    category = models.ForeignKey(
        'about.Category', on_delete=models.CASCADE, related_name="event_category", default=None, verbose_name=_("Category"))
    image = models.ImageField(
        upload_to='event/', default=None, verbose_name=_("Image"))
    date = models.DateField(verbose_name=_("Date"))

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")


class Subscriber(BaseModel):
    email = models.EmailField(verbose_name=_("Email"))

    def __str__(self) -> str:
        return f"{self.email}"

    class Meta:
        verbose_name = _("Abunəçi")
        verbose_name_plural = _("Abunəçilər")


class Dateofcreate(BaseModel):
    description = RichTextField(
        verbose_name=_("Description"), blank=True, null=True)

    def __str__(self) -> str:
        return 'Yaradilma tarixi'

    class Meta:
        verbose_name = _("Yaradilma tarixi")
        verbose_name_plural = _("Yaradilma tarixi")
