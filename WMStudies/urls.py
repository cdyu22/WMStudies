from django.contrib import admin
from django.urls import path

from MODULE_pages.views import home_view, classes_view, about_view, register_view,logout_view, phone_change_view

urlpatterns = [
    path('',          home_view,          name = ""),
    path("home/",     home_view,          name = "home" ),
    path('about/',    about_view,         name=  "about"),
    path('register/', register_view,      name = "register"),
    path('logout/',   logout_view, name = "logout"),

    path('classes/',  classes_view,       name = "classes"),
    path('phone_change/', phone_change_view, name="phone_change" ),
    path('admin/', admin.site.urls),
] 

#Can run code here ONCE
