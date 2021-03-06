# Generated by Django 3.2.13 on 2022-06-15 01:48

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novella', '0002_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cat_image',
            field=cloudinary.models.CloudinaryField(default='category_placeholder', max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='category',
            name='describe',
            field=models.TextField(default='this is a category text', max_length=200),
        ),
    ]
