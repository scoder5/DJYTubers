# Generated by Django 4.1.7 on 2023-03-16 11:47

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0002_alter_youtuber_camera_type_alter_youtuber_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
