from django.db import models

from kollec.utils.base_models import BaseModel
# Create your models here.


class Teacher(BaseModel):
    full_name = models.CharField(
        verbose_name='Full Name', max_length=50, default="")
    description = models.TextField(verbose_name='Description', blank=True)
    photo = models.ImageField(upload_to='teachers',
                              default='teachers/default.png')
    subject = models.ForeignKey(
        'Subject', on_delete=models.CASCADE, related_name='subject_teachers', default=1)

    def __str__(self):
        return self.full_name


class Subject(BaseModel):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
