from django.db import models
from datetime import datetime,date



# Create your models here.
class Users(models.Model):
    First_name = models.CharField(verbose_name= "Имя", max_length= 50)
    Last_name = models.CharField(verbose_name="Фамилия", max_length=50)
    Middle_name = models.CharField(verbose_name= "Отчество", max_length= 50)
    email = models.EmailField(verbose_name='e-mail',blank=True)
    birth_date = models.DateField(verbose_name="Дата рождения", default=date(2000,1,1))
    Date_in = models.DateField(verbose_name="Дата заселения",)
    Date_go = models.DateField(verbose_name="Дата выезда", )
    created_date = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    Date_update = models.DateTimeField(verbose_name="Дата изменения",auto_now=True)
    is_user = models.BooleanField(verbose_name="Заселен", default=True)
    def __str__(self):
        return self.Last_name