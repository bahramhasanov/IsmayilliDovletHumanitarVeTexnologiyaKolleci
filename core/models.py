from django.db import models
from django.db.models.fields.related import ForeignKey

from kollec.utils.base_models import BaseModel
# from app
from staff.models import Teacher


# Create your models here.


class Blog(models.Model): #blog
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=30)
    description = models.TextField(verbose_name="Description")
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, default="", related_name="teacher")

    def __str__(self) -> str:
        return f"{self.title}"


class Certificate(models.Model): #diplom
    pass