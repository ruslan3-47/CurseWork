# Generated by Django 5.1.3 on 2024-12-18 21:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sanatorium', '0023_users_first_name_users_last_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'ordering': ['last_name', 'first_name'], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='type',
            name='brify_description',
            field=models.CharField(default='кр опис', max_length=700, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='users',
            name='birth_date',
            field=models.DateField(default=datetime.date(2000, 1, 1), verbose_name='Дата рождения'),
        ),
    ]
