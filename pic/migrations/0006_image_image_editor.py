# Generated by Django 3.1.7 on 2021-03-21 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pic', '0005_image_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_editor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pic.editor'),
        ),
    ]
