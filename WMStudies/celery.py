from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab # scheduler


os.environ.setdefault('DJANGO_SETTINGS_MODULE','WMStudies.settings')
app = Celery('WMStudies', backend="rpc://", broker="pyamqp://")
app.conf.timezone = 'EST'
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'test': {
        'task': 'MODULE_scraping.tasks.scrape',
        'schedule': 75.0,
    },
}