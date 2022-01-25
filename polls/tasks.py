from celery import shared_task

from django.core.mail import send_mail as django_send_mail


@shared_task
def celery_send_mail(message, receiver):
    django_send_mail(['Promt!'], message, ['admin@example.com'], receiver)