# Generated by Django 2.2 on 2021-04-01 12:41

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pic', '0007_auto_20210401_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='picture',
        ),
        migrations.AlterField(
            model_name='image',
            name='pic',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='pic'),
        ),
    ]