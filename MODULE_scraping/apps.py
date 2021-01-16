from django.apps import AppConfig
import threading


class ScrappingConfig(AppConfig):
    name = 'MODULE_scraping'
    ran = False

    def ready(self):
        if ScrappingConfig.ran: 
            return
        ScrappingConfig.ran = True

        from .Subject_Driver import scrape
       
        thread1 = threading.Thread(target=scrape,daemon=True).start()