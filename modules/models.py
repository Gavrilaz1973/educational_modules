from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Module(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    preview = models.ImageField(upload_to='modules/', verbose_name='картинка', **NULLABLE)
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    link_to_materials = models.TextField(**NULLABLE, verbose_name='Ссылка на материалы')
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name='Пользователи', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'

