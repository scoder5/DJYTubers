# Generated by Django 4.1.7 on 2023-03-15 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0004_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='youtube_link',
            field=models.CharField(default='DEFAULT VALUE', max_length=255),
        ),
    ]