# Generated by Django 3.0.2 on 2020-01-21 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0005_auto_20200120_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='url',
            field=models.SlugField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]