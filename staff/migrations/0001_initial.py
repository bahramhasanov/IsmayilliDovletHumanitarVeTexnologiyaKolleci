# Generated by Django 3.2.8 on 2021-12-06 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='FBK',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('department_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='department', to='staff.department', verbose_name='department')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('fbk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groupfbk', to='staff.fbk', verbose_name='fbk')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('education', models.CharField(max_length=30)),
                ('age', models.IntegerField(blank=True, default=18, null=True)),
                ('level', models.CharField(blank=True, max_length=30, null=True, verbose_name='level')),
                ('description', models.TextField(verbose_name='description')),
                ('image', models.ImageField(null=True, upload_to='media/', verbose_name='Image')),
                ('fbk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacherfbk', to='staff.fbk', verbose_name='fbk')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='media/', verbose_name='Image')),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='group', to='staff.group', verbose_name='group')),
            ],
        ),
    ]
