from celery import shared_task
from django.core.mail import send_mail

from config import settings


@shared_task
def send_email(module, email):
    send_mail(
        subject='Открытие нового модуля',
        message=f"Открылся новый обучающий модуль: {module}",
        recipient_list=email,
        from_email=settings.EMAIL_HOST_USER
    )