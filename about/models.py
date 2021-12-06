from django.db import models

# import app
from kollec.utils.base_models import BaseModel


class Subject(models.Model):  # fenn
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.name}"


class Topic(models.Model):  # movzu
    name = models.CharField(max_length=30)
    description = models.TextField(verbose_name='Description')
    subject = models.ForeignKey(
        'about.Subject', on_delete=models.CASCADE, related_name="fenn", default=None)
    course_choices = (
        (1, 'I'),
        (2, 'II'),
        (3, 'III'),
        (4, 'IV'),
        (5, '9 illik baza'),
    )
    choices = models.IntegerField(
        choices=course_choices,
        default=5,
    )

    def __str__(self) -> str:
        return f"{self.name}"


class News(BaseModel):
    title = models.CharField(
        max_length=30, verbose_name='Title', help_text="Max 30 char.")
    description = models.TextField(verbose_name="Description")
    category = models.ForeignKey(
        'about.Category', on_delete=models.CASCADE, related_name="news_category", default=None)
    image = models.ImageField(upload_to='news/', default=None)

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"


class Category(BaseModel):
    title = models.CharField(
        max_length=30, verbose_name='Title', help_text="Max 30 char.")

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
