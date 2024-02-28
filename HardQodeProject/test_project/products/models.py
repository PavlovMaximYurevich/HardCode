from django.contrib.auth.models import AbstractUser
from django.db import models


class Creator(models.Model):
    first_name = models.CharField(
        'Имя создателя',
        max_length=100
    )
    second_name = models.CharField(
        "Фамилия создателя",
        max_length=150
    )


class Product(models.Model):
    author = models.ForeignKey(Creator,
                               on_delete=models.CASCADE,
                               verbose_name='Автор продукта'
                               )
    name = models.CharField('Наименование продукта',
                            unique=True,
                            max_length=100,
                            )
    date = models.DateTimeField('Дата старта')
    cost = models.FloatField('Стоимость')
    min_user = models.IntegerField(
        'Минимальное количество пользователей в группе')
    max_user = models.IntegerField(
        'Максимальное количество пользователей в группе')


class Group(models.Model):
    # student = models.M
    name = models.CharField('Наименование группы')
    product = models.ForeignKey(Product,
                                verbose_name = 'Принадлежность продукта к группе')
