from celery import shared_task
from celery import app

from .WM_Subject import Subject_Scraper
# from secrets.secrets import link, token, user_key

classes = Subject_Scraper( 2 )
print("IS THIS GETTING THRU???")
@shared_task
def scrape():
    classes.search()

# TODO: What I need to do now. We know that it's connected and correctly scraping the classes. At this point, we should
# try to follow the example online and create the models. We should see if there's a way to update instead of creating a new feed.
