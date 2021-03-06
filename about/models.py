import datetime
from io import BytesIO
from django.db import models
from ckeditor.fields import RichTextField
from matplotlib import image
from pytz import timezone

from kollec.utils.base_models import BaseModel
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.core.files import File
from PIL import Image


class FBKTeacher(BaseModel):
    full_name = models.CharField(max_length=255, verbose_name=_("Full name"))
    number = models.CharField(max_length=255, verbose_name=_("Number"))
    image = models.ImageField(upload_to='teachers', verbose_name=_("Image"))
    fbk = models.ForeignKey(
        "Faculty",
        on_delete=models.CASCADE,
        verbose_name=_("FBK"),
        related_name="teachers",
    )
    
    def __str__(self) -> str:
        return self.full_name
    
    class Meta:
        verbose_name = _("FBK teacher")
        verbose_name_plural = _("FBK teachers")


class News(BaseModel):
    title = models.CharField(
        max_length=100, verbose_name=_('Title'), help_text="Max 100 char.")
    # description = models.TextField(verbose_name="Description", null=True, blank=True)
    description = RichTextField(
        verbose_name=_("Description"), blank=True, null=True)
    category = models.ForeignKey(
        'about.Category', on_delete=models.CASCADE, related_name="news_category", default=None, verbose_name=_("Category"))
    image = models.ImageField(
        upload_to='news/', default=None, verbose_name=_("Image"))
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            now = datetime.datetime.now(timezone('Asia/Baku'))
            self.slug = slugify(f"{self.title}-{now}")
            # new_image = self.reduce_image_size(self.image)
            # self.image = new_image
        super().save(*args, **kwargs)

    def reduce_image_size(self, image):
        img = Image.open(image)
        rgb_im = img.convert('RGB')
        rgb_im.save(f'{image}.jpg')
        thumb_io = BytesIO()
        rgb_im.save(thumb_io, 'jpeg', quality=50)
        new_image = File(thumb_io, name=image.name)
        return new_image

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = _("X??b??r")
        verbose_name_plural = _("X??b??rl??r")


class Category(BaseModel):
    title = models.CharField(
        max_length=100, verbose_name=_('Title'), help_text="Max 100 char.")

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = _("Kateqoriya")
        verbose_name_plural = _("Kateqoriyalar")


class Faculty(BaseModel):
    title = models.CharField(
        max_length=100, verbose_name=_('Title'), help_text="Max 100 char.")
    description = RichTextField(
        verbose_name=_("Description"), blank=True, null=True)
    image = models.ImageField(upload_to='faculty/',
                              default=None, verbose_name=_("Image"))
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    department = models.ForeignKey(
        'staff.Department', on_delete=models.CASCADE, related_name="faculty_department", verbose_name=_("Department"), null=True, blank=True)
    def __str__(self) -> str:
        return f"{self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            now = datetime.datetime.now(timezone('Asia/Baku'))
            self.slug = slugify(f"{self.title}-{now}")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("FBK")
        verbose_name_plural = _("FBKlar")


class Specialty(BaseModel):
    title = models.CharField(
        max_length=100, verbose_name=_('Title'), help_text="Max 100 char.")
    description = RichTextField(
        verbose_name=_("Description"), blank=True, null=True)
    image_icon = models.ImageField(
        upload_to='specialty/', default=None, verbose_name=_("Image"))
    faculty = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, related_name="specialty_faculty", default=None, verbose_name=_("Faculty"))
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            now = datetime.datetime.now(timezone('Asia/Baku'))
            self.slug = slugify(f"{self.title}-{now}")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Ixtisas")
        verbose_name_plural = _("Ixtisaslar")


class Admissionrules(BaseModel):
    total_rules = RichTextField(
        verbose_name=_("General Admission"), blank=True, null=True)
    from_9_rules = RichTextField(
        verbose_name=_("From 9 Admission"), blank=True, null=True)
    from_11_rules = RichTextField(
        verbose_name=_("From 11 Admission"), blank=True, null=True)

    def __str__(self) -> str:
        return 'q??bul'

    class Meta:
        verbose_name = _("q??bul qaydalar??")
        verbose_name_plural = _("q??bul qaydalar??")


class About(BaseModel):
    title = models.CharField(
        max_length=100, verbose_name=_('Title'), help_text="Max 100 char.")
    description = RichTextField(
        verbose_name=_("Description"), blank=True, null=True)
    image = models.ImageField(
        upload_to='about/', default=None, verbose_name=_("Image"))
    ytb_link = models.CharField(
        max_length=100, verbose_name=_('Youtube Link'), help_text="Max 100 char.")

    def __str__(self) -> str:
        return 'Haqq??m??zda'

    class Meta:
        verbose_name = _("Haqq??m??zda")
        verbose_name_plural = _("Haqq??m??zda")


class Event(BaseModel):
    title = models.CharField(
        max_length=100, verbose_name=_('Title'), help_text="Max 100 char.")
    description = RichTextField(
        verbose_name=_("Description"))
    category = models.ForeignKey(
        'about.Category', on_delete=models.CASCADE, related_name="event_category", default=None, verbose_name=_("Category"))
    image = models.ImageField(
        upload_to='event/', default=None, verbose_name=_("Image"))
    date = models.DateTimeField(verbose_name=_("DateTime"))
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            now = datetime.datetime.now(timezone('Asia/Baku'))
            self.slug = slugify(f"{self.title}-{now}")
        super(Event, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")


class Subscriber(BaseModel):
    email = models.EmailField(verbose_name=_("Email"), unique=True)

    def __str__(self) -> str:
        return f"{self.email}"

    class Meta:
        verbose_name = _("Abun????i")
        verbose_name_plural = _("Abun????il??r")


class Dateofcreate(BaseModel):
    title = models.CharField(
        max_length=100, verbose_name=_('Title'), help_text="Max 100 char.")
    description = RichTextField(
        verbose_name=_("Description"), blank=True, null=True)

    def __str__(self) -> str:
        return 'Yaradilma tarixi'

    class Meta:
        verbose_name = _("Yaradilma tarixi")
        verbose_name_plural = _("Yaradilma tarixi")


class Practic(BaseModel):
    title = models.CharField(
        max_length=100, verbose_name=_('Title'), help_text="Max 100 char.")
    description = RichTextField(
        verbose_name=_("Description"), blank=True, null=True)
    image_icon = models.ImageField(
        upload_to='practic/', default=None, verbose_name=_("Image icon"))
    image = models.ImageField(
        upload_to='practic/', default=None, verbose_name=_("Image"))
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            now = datetime.datetime.now(timezone('Asia/Baku'))
            self.slug = slugify(f"{self.title}-{now}")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Practic")
        verbose_name_plural = _("Practies")


class PracticPlace(BaseModel):
    title = models.CharField(
        max_length=100, verbose_name=_('Title'), help_text="Max 100 char.")
    description = RichTextField(
        verbose_name=_("Description"), blank=True, null=True)
    practic = models.ForeignKey(
        Practic, on_delete=models.CASCADE, related_name="practic_place", default=None, verbose_name=_("Practic"))

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = _("Practic Place")
        verbose_name_plural = _("Practic Places")


class Gallery(BaseModel):
    name = models.CharField(
        max_length=100, verbose_name=_('Title'), help_text="Max 100 char."
    )
    image = models.ImageField(
        upload_to='gallery/', default=None, verbose_name=_("Image"))

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name = _("Gallery")
        verbose_name_plural = _("Galleries")


class CareerSupport(BaseModel):
    description = RichTextField(
        verbose_name=_("Description"), blank=True, null=True)

    def __str__(self) -> str:
        return 'Career support'

    class Meta:
        verbose_name = _("karyera d??st??yi")
        verbose_name_plural = _("karyera d??st??yi")


class Testimonial(BaseModel):
    image = models.ImageField(upload_to='testimonal/',
                              default=None, verbose_name=_("Image"))
    name = models.CharField(
        max_length=100, verbose_name=_('name'), help_text="Max 100 char."
    )
    surname = models.CharField(
        max_length=100, verbose_name=_('surname'), help_text="Max 100 char.",
    )
    status = models.CharField(
        max_length=100, verbose_name=_('status'), help_text="Max 100 char."
    )
    description = RichTextField(
        verbose_name=_("Description"), blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name = _("Testimonial")
        verbose_name_plural = _("Testimonials")


class Contact(BaseModel):
    title = models.CharField(
        max_length=100, verbose_name=_('Title'), help_text="Max 100 char.")
    address = RichTextField(
        verbose_name=_("Address"), blank=True, null=True)
    phone = models.CharField(
        max_length=100, verbose_name=_('Phone'), help_text="Max 100 char.")
    email = models.EmailField(verbose_name=_("Email"))

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = _("??laq??")
        verbose_name_plural = _("??laq??")
