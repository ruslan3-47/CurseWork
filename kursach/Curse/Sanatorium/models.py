
from django.db import models
from datetime import date

from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(verbose_name="Имя", blank= True, null =True, max_length=50)
    last_name = models.CharField(verbose_name="Фамилия",blank = True, null=True, max_length=50)
    middle_name = models.CharField(verbose_name="Отчество", max_length=50,blank = True, null=True)
    birth_date = models.DateField(verbose_name="Дата рождения", default=date(2000, 1, 1))
    create_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Дата изменения ", auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.user.last_name}'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['last_name', 'first_name']


class Room(models.Model):
    type = models.ForeignKey('Type', on_delete=models.CASCADE, verbose_name="Тип комнаты")
    image = models.ImageField(upload_to="media/", blank=True, default="media/mask")
    is_order = models.BooleanField(verbose_name="занят", default=False)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)

    def get_absolute_url(self):
        return reverse('room', kwargs={'room_slug': self.slug})

    def __str__(self):
        return f'{self.pk} - {self.type}'

    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "комнаты"


class Program(models.Model):
    name = models.CharField(verbose_name="Название программы", max_length=50)
    price = models.DecimalField(verbose_name="Цена", max_digits=15, decimal_places=2)
    description = models.CharField(verbose_name="Описание", max_length=2000, null=True, default="Тут будет описание")
    date = models.IntegerField(verbose_name="Дата проведения", null=True)
    briefly_description = models.CharField(verbose_name="Краткое описание", max_length=1200, null=True,
                                           default="Краткое описание")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', null=True)

    def get_absolute_url(self):
        return reverse('program', kwargs={'program_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Программа"
        verbose_name_plural = "Программы"


class Type(models.Model):
    name = models.CharField(verbose_name="Тип комнаты", max_length=50)
    price = models.DecimalField(verbose_name="Цена за ночь", max_digits=15, decimal_places=2)
    description = models.CharField(verbose_name="Описание", max_length=1000, default="ничего")
    brify_description = models.CharField(verbose_name="Краткое описание", max_length=300, default="кр опис")

    def __str__(self):
        return f'{self.name} - {self.price}'

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"


class Order(models.Model):
    program_name = models.ForeignKey('Program', verbose_name="Название программы", on_delete=models.CASCADE)
    room_id = models.ForeignKey('Room', verbose_name="Номер комнаты", on_delete=models.CASCADE)
    date_in = models.DateField(verbose_name="День заселения", default=date(2000, 1, 1))
    date_out = models.DateField(verbose_name="День выселения", default=date(2000, 2, 1))
    price = models.DecimalField(verbose_name="Стоимость", max_digits=15, decimal_places=2, blank=True, null=True)
    user_id = models.ForeignKey('Users', verbose_name="Клиент", null=True, blank=True, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.date_in and self.date_out and self.program_name and self.room_id:
            date = (self.date_out - self.date_in).days
            program_price = self.program_name.price
            room_price = self.room_id.type.price
            self.price = program_price + (room_price * date)

        return super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f"Бронь номер - {Order.pk}"

    class Meta:
        verbose_name = "Бронь"
        verbose_name_plural = "Заказы"
# add model for user
