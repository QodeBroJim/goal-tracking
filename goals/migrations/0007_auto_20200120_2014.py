# Generated by Django 3.0.2 on 2020-01-21 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0006_category_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='url',
            field=models.SlugField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='url',
            field=models.SlugField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]