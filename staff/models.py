from django.db import models
from ckeditor.fields import RichTextField
from kollec.utils.base_models import BaseModel
# Create your models here.


class Teacher(BaseModel):
    full_name = models.CharField(
        verbose_name='Full Name', max_length=50, default="")
    description = RichTextField(
        verbose_name="Description", blank=True, null=True)
    photo = models.ImageField(upload_to='teachers',
                              default='teachers/default.png')
    subject = models.ForeignKey(
        'Subject', on_delete=models.CASCADE, related_name='subject_teachers', default=1)

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = 'Müəllim'
        verbose_name_plural = 'Müəllimlər'


class Subject(BaseModel):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Fənn'
        verbose_name_plural = 'Fənnlər'


class PDF(BaseModel):
    title = models.CharField(
        max_length=50, verbose_name='Title', help_text="Max 50 char.")
    category = models.ForeignKey(
        'staff.Subject', on_delete=models.CASCADE, related_name="pdf_category", default=None)
    file = models.FileField(upload_to='pdf/', default=None)

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = "PDF"
        verbose_name_plural = "PDFs"
