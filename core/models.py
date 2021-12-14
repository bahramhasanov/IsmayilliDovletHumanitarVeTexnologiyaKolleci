from django.db import models
from ckeditor.fields import RichTextField

from kollec.utils.base_models import BaseModel


class Mostquestions(BaseModel):
    title = models.CharField(max_length=100, verbose_name='Sual')
    description = RichTextField(
        verbose_name="Cavab", blank=True, null=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Sual'
        verbose_name_plural = 'Suallar'


class Subscrib(BaseModel):
    email = models.EmailField(verbose_name="Email", unique=True)

    def __str__(self) -> str:
        return self.email
    
    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'