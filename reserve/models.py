from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Reserve(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    phone = models.CharField(max_length=11, verbose_name='شماره تلفن')
    number = models.IntegerField(verbose_name='تعداد نفرات')
    date = models.DateField(auto_now=False, auto_now_add=False, default='2023-01-01' , verbose_name='روز')
    time = models.TimeField(auto_now=False, auto_now_add=False,  default='11:45:23', verbose_name='زمان')

    def __str__(self) -> str:
        return self.name