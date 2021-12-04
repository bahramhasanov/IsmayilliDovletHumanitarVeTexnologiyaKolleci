from django.db import models
from django.db.models.fields.related import ForeignKey

from kollec.utils.base_models import BaseModel
# from app
from staff.models import Teacher


class Blog(models.Model): #blog
    title = models.CharField(max_length=30, verbose_name='Title' , help_text="Max 30 char.")
    subtitle = models.CharField(max_length=30, help_text="Max 80 char.")
    description = models.TextField(verbose_name="Description")
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, default="", related_name="teacher")
    images = models.ManyToManyField('core.BlogImage', related_name="blog")
    
    def __str__(self) -> str:
        return f"{self.title}"
    
    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blog"
        

class BlogImage(models.Model): #blog_image
    image = models.ImageField(verbose_name="Image",
                              upload_to="media/", null=True, blank=True)

    

class Certificate(models.Model): #diplom
    pass
