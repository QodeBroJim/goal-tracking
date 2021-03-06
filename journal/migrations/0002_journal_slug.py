# Generated by Django 3.0.2 on 2020-01-12 23:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=250, unique_for_date='timestamp'),
            preserve_default=False,
        ),
    ]
