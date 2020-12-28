from django.shortcuts import render
from django.http import HttpResponse

def home_view(request,*args, **kwargs):
    return render(request,"home.html",{})

def classes_view(request,*args, **kwargs):
    return render(request, "classes.html",{})

def about_view(request, *args, **kwargs): 
    my_context = {
        "akey":"This is about this site",
        "anumber": 100,
        "alist" : [ 123, 456, 789],
    }
    return render(request,"about.html", my_context)

def register_view(request,*args, **kwargs):
    my_context = {}
    return render(request, "register.html")