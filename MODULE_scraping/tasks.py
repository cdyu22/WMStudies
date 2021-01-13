from celery import shared_task
from celery import app

from .WM_Subject import Subject_Scraper
# from secrets.secrets import link, token, user_key

classes = Subject_Scraper( 2 )
print("Created a new instance of the subject scraper (tasks.py)")

@shared_task
def scrape():
    classes.search()

