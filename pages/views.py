from pages.forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

def home_view(request,*args, **kwargs):
    if request.method == "GET":
        return render(request, "home.html")

    elif request.method == "POST":
        
        user = request.POST.get('UserId')
        passw = request.POST.get('Password')
        user = authenticate(request, username = user, password = passw )
        if user is not None: 
            login(request, user)
            return render(request, "home.html")   
        return render(request, "about.html",{})
        
        
    # return render(request, "home.html")

def classes_view(request,*args, **kwargs):
    return render(request, "classes.html",{})

def about_view(request, *args, **kwargs): 
    my_context = {
        "akey":"This is about this site",
        "anumber": 100,
        "alist" : [ 123, 456, 789],
    }
    return render(request,"about.html", my_context)

def register_view(request, *args, **kwargs):
    my_context = {}
    if request.method == "GET":
        return render(request, "register.html", {"form": CustomUserCreationForm})
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect(reverse("home"))

def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect(reverse("home"))