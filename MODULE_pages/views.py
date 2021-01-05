from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from MODULE_users.forms import UserAdminCreationForm

def home_view( request, *args, **kwargs ):
    if request.method == "GET":
        return render( request, "home.html", {} )

    elif request.method == "POST":
        user = request.POST.get( 'UserId' )
        password1 = request.POST.get( 'Password' )

        user = authenticate( request, username = user, password = password1 )

        if user is not None: 
            login( request, user )
            return render( request, "home.html" )   
        else:
            messages.error( request, 'Username or Password is not Correct.' )
            return redirect( reverse( "home" ), {} ) 

def register_view(request, *args, **kwargs):
    if request.method == "GET":
        return render( request, "register.html", {"form": UserAdminCreationForm } )

    elif request.method == "POST":
        form = UserAdminCreationForm( request.POST )

        if form.is_valid():
            user = form.save()
            login( request, user )
            return redirect( reverse( "home" ) )

def logout_view( request, *args, **kwargs ):
    logout( request )
    return redirect( reverse( "home" ) )


# TODO:: IMPLEMENT

def classes_view(request,*args, **kwargs):
    return render(request, "classes.html",{})

def about_view(request, *args, **kwargs): 
    my_context = {
        "akey":"This is about this site",
        "anumber": 100,
        "alist" : [ 123, 456, 789],
    }
    return render(request,"about.html", my_context)

