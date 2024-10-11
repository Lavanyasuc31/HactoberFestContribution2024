from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab, schedule

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job_alert_core.settings')

# Create the Celery application
app = Celery('job_alert_core')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

#Celery Beat Settings
app.conf.beat_schedule  = {
    'scrap-jobs-every-5-minutes': {
        'task': 'Job_Alert.tasks.scrape_jobs',
        'schedule': schedule(300),
        #'args': (2,) pass any arguments
    }
}


# Automatically discover tasks from all installed apps
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}') 
 