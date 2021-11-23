from django.db import models
from django.db.models.fields.related import ForeignKey

from kollec.utils.base_models import BaseModel
# from app
from staff.models import Teacher


class Blog(models.Model): #blog
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=30)
    description = models.TextField(verbose_name="Description")
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, default="", related_name="teacher")
    # image = models.ImageField(upload_to='blog_images', blank=True)

    def __str__(self) -> str:
        return f"{self.title}"

# class BlogImage(models.Model): #blog_image
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE, default="", related_name="blogimg")
#     image = models.ImageField(upload_to='blog_images/', verbose_name="Image")

#     def __str__(self) -> str:
#         return f"{self.blog.title} - {self.image}"

class Certificate(models.Model): #diplom
    pass
