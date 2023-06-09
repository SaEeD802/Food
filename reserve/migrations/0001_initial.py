# Generated by Django 4.1.7 on 2023-04-28 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('phone', models.CharField(max_length=11, verbose_name='شماره تلفن')),
                ('number', models.IntegerField(verbose_name='تعداد نفرات')),
                ('date', models.DateField(verbose_name='روز')),
                ('time', models.TimeField(verbose_name='زمان')),
            ],
        ),
    ]
