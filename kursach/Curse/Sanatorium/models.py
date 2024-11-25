from django.db import models
from datetime import date

from django.urls import reverse


# Create your models here.

class Users(models.Model):
    first_name = models.CharField(verbose_name="Имя", max_length=50)
    last_name = models.CharField(verbose_name="Фамилия", max_length=50)
    middle_name = models.CharField(verbose_name="Отчество", max_length=50)
    email = models.EmailField(verbose_name="e-mail", blank= True)
    birth_date = models.DateField(verbose_name="День рождения", default=date(2000,1,1))
    is_in = models.BooleanField(verbose_name="Заселен",default=True)
    date_in = models.DateField(verbose_name="День заселения", default=False)
    date_out = models.DateField(verbose_name="День выселения", default=False)
    room= models.ForeignKey('Room', on_delete=models.CASCADE, verbose_name="Комната")
    program = models.ForeignKey('Program', on_delete=models.CASCADE, verbose_name="Программа")
    create_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Дата изменения ", auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['last_name', 'first_name']


class Room(models.Model):
    type = models.ForeignKey('Type',on_delete=models.CASCADE, verbose_name="Тип комнаты")
    image = models.ImageField(upload_to="media/", blank = True,default="media/mask")
    slug = models.SlugField(max_length= 255,unique=True, db_index=True, verbose_name="URL", null=True)

    def get_absolute_url(self):
        return reverse('room', kwargs={'room_slug':self.slug})

    def __str__(self):
        return f'{self.pk} - {self.type}'

    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "комнаты"


class Program(models.Model):
    name = models.CharField(verbose_name="Название программы", max_length=50)
    price = models.DecimalField(verbose_name="Цена", max_digits=15, decimal_places=2)

    def __str__(self):
        return f'{self.name} - {self.price}'

    class Meta:
        verbose_name = "Программа"
        verbose_name_plural = "Программы"


class Type(models.Model):
    name = models.CharField(verbose_name="Тип комнаты", max_length=50)
    price = models.DecimalField(verbose_name="Цена за ночь", max_digits=15, decimal_places=2)
    description = models.CharField(verbose_name="Описание", max_length=1000, default="ничего")

    def __str__(self):
        return f'{self.name} - {self.price}'

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"