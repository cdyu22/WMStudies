"""WMStudies URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
import django.contrib.auth.urls

from pages.views import home_view, classes_view, about_view, register_view,logout_view
from django.conf.urls import url
# from users.views import dashboard

# from clients.views import person_detail_view

urlpatterns = [
    # url(r"^register/", register_view, name="register"),
    path('',          home_view,          name = ""),
    path("home/",     home_view,          name = "home" ),
    path('about/',    about_view,         name=  "about"),
    path('register/', register_view,      name = "register"),
    path('logout/',   logout_view, name = "logout"),

    path('classes/',  classes_view,       name = "classes"),
    

    # path('detail/',   person_detail_view, name="detail"),

    path('admin/', admin.site.urls),
] 
