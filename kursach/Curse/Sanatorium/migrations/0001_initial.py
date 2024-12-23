# Generated by Django 5.1.3 on 2024-11-18 16:11

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Тип комнаты')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Цена за ночь')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Цена за ночь')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sanatorium.type', verbose_name='Тип комнаты')),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название программы')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Цена')),
                ('type_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sanatorium.type', verbose_name='Тип комнаты')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('middle_name', models.CharField(max_length=50, verbose_name='Отчество')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='e-mail')),
                ('birth_date', models.DateField(default=datetime.date(2000, 1, 1), verbose_name='День рождения')),
                ('is_in', models.BooleanField(default=True, verbose_name='Заселен')),
                ('date_in', models.DateField(default=False, verbose_name='День заселения')),
                ('date_out', models.DateField(default=False, verbose_name='День выселения')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения ')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sanatorium.program', verbose_name='Программа')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sanatorium.room', verbose_name='Комната')),
            ],
        ),
    ]
