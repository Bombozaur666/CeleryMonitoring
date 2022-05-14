import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CeleryMonitoring.settings')

app = Celery('CeleryMonitoring')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'every-1-minute': {
        'task': 'MonitoringManager.tasks.checkWebsites',
        'schedule': 5,
        'args':('01')
    }
}
"""
app.conf.beat_schedule = {
    'every-5-minutes': {
        'task': 'MonitoringManager.tasks.checkWebsites',
        'schedule': 300,
        'args': ('05')
    }
}
app.conf.beat_schedule = {
    'every-15-minutes': {
        'task': 'MonitoringManager.tasks.checkWebsites',
        'schedule': 900,
        'args': ('15')
    }
}
app.conf.beat_schedule = {
    'every-30-minutes': {
        'task': 'MonitoringManager.tasks.checkWebsites',
        'schedule': 1800,
        'args': ('30')
    }
}
app.conf.beat_schedule = {
    'every-60-minutes': {
        'task': 'MonitoringManager.tasks.checkWebsites',
        'schedule': 3600,
        'args': ('60')
    }
}"""