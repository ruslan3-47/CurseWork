# Generated by Django 5.1.3 on 2024-11-25 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sanatorium', '0004_type_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='description',
            field=models.CharField(default='ничего', max_length=500, verbose_name='Описание'),
        ),
    ]