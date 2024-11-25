# Generated by Django 5.1.3 on 2024-11-25 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sanatorium', '0007_type_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='URL'),
        ),
    ]