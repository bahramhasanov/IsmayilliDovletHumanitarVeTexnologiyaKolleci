# Generated by Django 3.2.8 on 2021-11-01 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_rename_img_new_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='images',
        ),
        migrations.AddField(
            model_name='new',
            name='img',
            field=models.ManyToManyField(related_name='image', to='about.NewsImage'),
        ),
    ]
