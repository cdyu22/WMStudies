from django.contrib import admin
from django.urls import path

from MODULE_pages.views import home_view, classes_view, about_view, register_view,logout_view

urlpatterns = [
    path('',          home_view,          name = ""),
    path("home/",     home_view,          name = "home" ),
    path('about/',    about_view,         name=  "about"),
    path('register/', register_view,      name = "register"),
    path('logout/',   logout_view, name = "logout"),

    path('classes/',  classes_view,       name = "classes"),

    path('admin/', admin.site.urls),
] 

#Can run code here ONCE
#Saving this, can loop through stuff
# from MODULE_users.models import User
# from MODULE_scraping.WM_Subject import Subject_Scraper
# print(User.objects.all())
# c = Subject_Scraper(2)

