from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    name = models.CharField(max_length=100, verbose_name='Имя', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='почта')


    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
