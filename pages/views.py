from django.shortcuts import render
from django.http import HttpResponse

def home_view(*args, **kwargs):
    return HttpResponse("<h1>Hello World!!!</h1>")

def client_view(*args, **kwargs):
    return HttpResponse("<h1>More Stuff to Come!</h1>")

def template_view(request,*args, **kwargs): #To test
    return render(request,"home.html",{})
