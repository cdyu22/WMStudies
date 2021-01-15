from django.apps import AppConfig
import threading


class ScrappingConfig(AppConfig):
    name = 'MODULE_scraping'
    ran = False

    def ready(self):
        if ScrappingConfig.ran: 
            return
        ScrappingConfig.ran = True
        # from .models import Course

        from .Subject_Driver import scrape
        print("RUNNING SCRAPPING CONFIG READY FUNCTIOn")
       
        thread1 = threading.Thread(target=scrape,daemon=True).start()
        # print(Course.objects.get(CRN = 21533).course_name)