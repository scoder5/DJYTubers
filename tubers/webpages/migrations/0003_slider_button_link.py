# Generated by Django 4.1.7 on 2023-03-12 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0002_rename_phot_slider_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='button_link',
            field=models.CharField(default='DEFAULT VALUE', max_length=255),
        ),
    ]
