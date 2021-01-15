from .WM_Subject import Subject_Scraper
# import requests

def scrape():
    while(True):
        try:
            # req = requests.post(link, data = {'token' : token,'user' : user_key,'message' : "Started search."})
            classes = Subject_Scraper(  2 )
            classes.search()
        except Exception as e:
            print(e)
            # req = requests.post(link, data = {'token' : token,'user' : user_key,'message' : str(e)})