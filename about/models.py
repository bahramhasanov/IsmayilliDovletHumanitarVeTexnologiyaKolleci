from django.db import models
from ckeditor.fields import RichTextField

from kollec.utils.base_models import BaseModel


class News(BaseModel):
    title = models.CharField(
        max_length=30, verbose_name='Title', help_text="Max 30 char.")
    description = models.TextField(verbose_name="Description", null=True, blank=True)
    # description = RichTextField(verbose_name="Description", blank=True, null=True),
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
