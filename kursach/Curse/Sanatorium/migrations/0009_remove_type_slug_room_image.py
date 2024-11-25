# Generated by Django 5.1.3 on 2024-11-25 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sanatorium', '0008_alter_type_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='type',
            name='slug',
        ),
        migrations.AddField(
            model_name='room',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
