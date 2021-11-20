from django.db import models

from kollec.utils.base_models import BaseModel
# Create your models here.


class Teacher(models.Model):  # muellim
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    education = models.CharField(max_length=30)
    age = models.IntegerField(default=18, null=True, blank=True)
    level = models.CharField(max_length=30, verbose_name="level", null=True, blank=True)
    description = models.TextField(verbose_name="description")
    image = models.ImageField(verbose_name="Image",
                              upload_to="media/", null=True)
    fbk = models.ForeignKey('staff.FBK', related_name='teacherfbk',
                            on_delete=models.CASCADE, verbose_name="fbk")

    def __str__(self) -> str:
        return f"{self.name}"


class FBK(models.Model):  # fbk
    name = models.CharField(max_length=30)
    department_id = models.ForeignKey(
        'staff.Department', related_name='department', on_delete=models.CASCADE, verbose_name="department", default='')

    def __str__(self) -> str:
        return f"{self.name}"


class Department(models.Model):  # şöbə
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.name}"


class Student(models.Model):  # telebe
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    image = models.ImageField(verbose_name="Image",
                              upload_to="media/", null=False)
    group = models.OneToOneField(
        'staff.Group', related_name='group', on_delete=models.CASCADE, verbose_name="group")

    def __str__(self) -> str:
        return f"{self.name}"


class Group(models.Model):  # qrup
    name = models.CharField(max_length=30)
    fbk = models.ForeignKey('staff.FBK', related_name='groupfbk',
                            on_delete=models.CASCADE, verbose_name="fbk")

    def __str__(self) -> str:
        return f"{self.name}"


# class Image_student(models.Model):  # telebe shekilleri
#     image = models.ImageField(verbose_name="Image",
#                               upload_to="media/", null=True)
#     students = models.ForeignKey(
#         'staff.Student', on_delete=models.CASCADE, verbose_name="students image", related_name="student_images")

#     def __str__(self) -> str:
#         return f"{self.image}"


# class Image_teacher(models.Model):  # muellim shekilleri
#     image = models.ImageField(verbose_name="Image",
#                               upload_to="media/", null=False)
#     teacher = models.ForeignKey(
#         'staff.Teacher', default=None, on_delete=models.CASCADE, verbose_name="teacher image", related_name="teacher_images")

#     def __str__(self) -> str:
#         return f"{self.image}"
