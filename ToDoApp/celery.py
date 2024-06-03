import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ToDoApp.settings')

app = Celery('ToDoApp')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


from celery.schedules import crontab

app.conf.beat_schedule = { #celery -A proj beat
    # Executes every Monday morning at 7:30 a.m. static way of sending tasks
    'send-notification-every-minute': {
        'task': 'ToDo_App.tasks.send_notification',
        'schedule': crontab(), #tell the users specified hours and define them here
        'args': ('users_mail'),
    },
}
app.conf.timezone = 'UTC'
