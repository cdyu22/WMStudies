from .WM_Subject import Subject_Scraper

def scrape():
    while(True):
        try:
            classes = Subject_Scraper(  2 )
            classes.search()
        except Exception as e:
            print(e)