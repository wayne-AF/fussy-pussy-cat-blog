# Generated by Django 3.2.16 on 2023-01-21 16:02

from django.db import migrations
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=django_summernote.fields.SummernoteTextField(),
        ),
    ]