# Generated by Django 3.2.16 on 2023-01-24 18:24

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/ddaxhspml/image/upload/v1674583724/static/static-images/default_profile_image.f724bc1fa3df.png', max_length=255, verbose_name='image'),
        ),
    ]
