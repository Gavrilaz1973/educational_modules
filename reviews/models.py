from django.db import models

from config import settings
from modules.models import Module

NULLABLE = {'blank': True, 'null': True}


class Review(models.Model):
    METHOD_CHOICES = [('1', '1'), ('2', '2'), ('3', '3'),('4', '4'),('5', '5'),]
    rating = models.CharField(choices=METHOD_CHOICES, default=METHOD_CHOICES[0], verbose_name='рейтинг', **NULLABLE)
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    module = models.ForeignKey(Module, on_delete=models.CASCADE, verbose_name='Модуль', **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)

    def __str__(self):
        return self.rating

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

