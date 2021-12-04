from django.db import models

# import app
from kollec.utils.base_models import BaseModel


course_choices = (
        (1, 'I'),
        (2, 'II'),
        (3, 'III'),
        (4, 'IV'),
        (5, '9 illik baza'), 
    )

class Subject(models.Model): #fenn
    name = models.CharField(max_length=30)  
       
    def __str__(self) -> str:
        return f"{self.name}"


class Topic(models.Model): # movzu
    name = models.CharField(max_length=30)
    description = models.TextField(verbose_name='Description')
    subject = models.ForeignKey('about.Subject',on_delete=models.CASCADE, related_name="fenn", default=None)
    choices = models.IntegerField(
        choices=course_choices,
        default=5,
    )
    
    def __str__(self) -> str:
        return f"{self.name}"


class News(BaseModel):  # news, xeber
    name = models.CharField(max_length=30,verbose_name='Title' , help_text="Max 30 char.")
    subtitle = models.CharField(
        verbose_name="Subtitle", max_length=80, help_text="Max 80 char.")
    description = models.TextField(verbose_name="Description")
    images = models.ManyToManyField(
        'about.NewsImage', related_name="news")
     
    
    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
 
    
class NewsImage(BaseModel):
    name = models.CharField(max_length=30, help_text="Max 30 char.")
    image = models.ImageField(verbose_name="Image",
                              upload_to="media/", null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"   
    
# qs = New.objects.order_by('created_at')[0:3][::-1]
