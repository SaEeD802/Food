from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Food(models.Model):
    FOODS = [
        ('iranifood', 'غذای ایرانی'),
        ('fastfood', 'فست فود'),
        ('juices', 'نوشیدنی'),
    ]

    name = models.CharField(max_length=100, verbose_name='نام غذا' )
    text = models.CharField(_('توضیحات'), max_length=100)
    price = models.IntegerField(default=100000, verbose_name='قیمت')
    time = models.IntegerField(default=2, verbose_name='زمان آماده سازی')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    image = models.ImageField(upload_to='webs/', verbose_name='عکس غذا')
    type_food = models.CharField(max_length=20, choices=FOODS, default='fastfood', verbose_name='نوع غذا')

    def __str__(self) -> str:
        return self.name