# Generated by Django 3.2.8 on 2021-11-01 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_rename_images_new_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new',
            old_name='img',
            new_name='images',
        ),
    ]
