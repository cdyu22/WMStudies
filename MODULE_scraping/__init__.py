from .WM_Subject import Subject_Scraper
from ..secrets.secrets import link, token, user_key
print("LOADED MODULE_SCRAPING")

classes = Subject_Scraper(  2, link, token, user_key )