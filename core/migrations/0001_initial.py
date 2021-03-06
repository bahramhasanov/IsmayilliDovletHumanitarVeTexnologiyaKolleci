# Generated by Django 3.2.8 on 2022-03-23 18:50

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('name_en', models.CharField(max_length=100, null=True, verbose_name='Name')),
                ('name_az', models.CharField(max_length=100, null=True, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=100, null=True, verbose_name='Name')),
                ('slogan', ckeditor.fields.RichTextField(verbose_name='Slogan')),
                ('slogan_en', ckeditor.fields.RichTextField(null=True, verbose_name='Slogan')),
                ('slogan_az', ckeditor.fields.RichTextField(null=True, verbose_name='Slogan')),
                ('slogan_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Slogan')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='description')),
                ('description_en', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='description')),
                ('description_az', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='description')),
                ('description_ru', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='main_page/', verbose_name='Image')),
                ('active_student_number', models.IntegerField()),
                ('faculty_number', models.IntegerField()),
                ('graduate_number', models.IntegerField()),
            ],
            options={
                'verbose_name': 'MainPage',
                'verbose_name_plural': 'MainPage',
            },
        ),
        migrations.CreateModel(
            name='Mostquestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('title_en', models.CharField(max_length=100, null=True, verbose_name='Title')),
                ('title_az', models.CharField(max_length=100, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=100, null=True, verbose_name='Title')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Cavab')),
                ('description_en', ckeditor.fields.RichTextField(null=True, verbose_name='Cavab')),
                ('description_az', ckeditor.fields.RichTextField(null=True, verbose_name='Cavab')),
                ('description_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Cavab')),
            ],
            options={
                'verbose_name': 'Sual',
                'verbose_name_plural': 'Suallar',
            },
        ),
    ]
