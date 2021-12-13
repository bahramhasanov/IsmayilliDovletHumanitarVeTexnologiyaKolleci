from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.fields.related import OneToOneField

from kollec.utils.base_models import BaseModel
from staff.models import Teacher

class News(BaseModel):
    title = models.CharField(
        max_length=30, verbose_name='Title', help_text="Max 30 char.")
    # description = models.TextField(verbose_name="Description", null=True, blank=True)
    description = RichTextField(
        verbose_name="Description", blank=True, null=True)
    category = models.ForeignKey(
        'about.Category', on_delete=models.CASCADE, related_name="news_category", default=None)
    image = models.ImageField(upload_to='news/', default=None)

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = "Xəbərlər"
        verbose_name_plural = "Xəbərlər"


class Category(BaseModel):
    title = models.CharField(
        max_length=30, verbose_name='Title', help_text="Max 30 char.")

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = "Kateqoriya"
        verbose_name_plural = "Kateqoriyalar"

        
class Faculty(BaseModel):
    title = models.CharField(
        max_length=30, verbose_name='Title', help_text="Max 30 char.")
    description = RichTextField(
        verbose_name="Description", blank=True, null=True)
    image = models.ImageField(upload_to='faculty/', default=None)
    # FBK = models.OneToOneField(Teacher, on_delete=models.CASCADE, related_name='faculty_teacher', default=1, null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = "FBK"
        verbose_name_plural = "FBK"


class Specialty(BaseModel):
    title = models.CharField(
        max_length=30, verbose_name='Title', help_text="Max 30 char.")
    description = RichTextField(
        verbose_name="Description", blank=True, null=True)
    image_icon = models.ImageField(upload_to='specialty/', default=None)
    faculty = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, related_name="specialty_faculty", default=None)

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = "Ixtisas"
        verbose_name_plural = "Ixtisaslar"

class Admissionrules(BaseModel):
    total_rules = RichTextField(
        verbose_name="Description", blank=True, null=True)
    from_9_rules = RichTextField(
        verbose_name="Description", blank=True, null=True)
    from_11_rules = RichTextField(
        verbose_name="Description", blank=True, null=True)
    
    def __str__(self) -> str:
        return 'qəbul'

    class Meta:
        verbose_name = "qəbul qaydaları"
        verbose_name_plural = "qəbul qaydaları"