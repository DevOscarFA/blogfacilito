# Generated by Django 2.1.3 on 2018-12-28 03:33

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(default='null'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
    ]