# feedback/tasks.py
import profile
from time import timezone


import datetime

from celery import shared_task
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

from ToDoApp.celery import app


@shared_task
def send_notification(users_mail):

    subject = 'Notification reminder'
    message = 'This is a kind reminder to get your texts finished.'
    email_from = settings.EMAIL_HOST_USER
    recipient = (users_mail,)  # profile_obj.email
    send_mail(subject, message, email_from, recipient)


@shared_task
def send_notification_2():
    print('helllo world again')


@shared_task
def send_pending_notifications():
    send_notification()
