from datetime import datetime, timedelta

from celery import shared_task

from django.core.mail import send_mail


@shared_task
def clean_logs():
    from students_tracker.models import Logger
    logger_list = Logger.objects.filter(created__lte=datetime.now() - timedelta(days=7))
    logger_list.delete()


@shared_task
def send_mail_async(param):
    send_mail(
        param['title'],
        param['message'],
        param['email_from'],
        ['dmytro.kaminskyi92@gmail.com'],
        fail_silently=False,
    )
