# feedback/tasks.py
import profile
from time import timezone

from celery import Celery


import datetime
from django.core.mail import send_mail
from django.conf import settings
app = Celery('ToDoApp')
@app.task(name='send_notification')
def send_notification():
    # try:
        #
        # profile_obj = Profile.objects.filter(is_completed=False)
        # for profile_obj in profile_obj:
        subject = 'Notification reminder'
        message = 'please finish your task'
        email_from = settings.EMAIL_HOST_USER
        recipient = 'alonxd124@gmail.com'  # profile_obj.email
        send_mail(subject, message, email_from, recipient)
    # except Exception as e:
    #     print(e)
