from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from MODULE_scraping.models import Course
from MODULE_users.models import User
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


def classes_view(request,*args, **kwargs):
    if request.user.is_authenticated:
        
        my_context = {}
        try: 
            curr_user = User.objects.get(username=request.user)
            # print(curr_user.course_set.all())
            for object in curr_user.course_set.all():
                my_context[ object.CRN ] =  [ object.section, object.course_name, object.status ]
            
        except AttributeError as e:
            print("User doesn't have any courses YET")
            print(e)
        except Exception as e:
            print("EXCEPTION!")
            print(e)
        if request.method == "POST":
            CRN = request.POST.get( 'CRN' )
            if Course.objects.filter(CRN=CRN).exists():
                specified_class = Course.objects.get(CRN=CRN)
                to_add = User.objects.get(username=request.user)
                specified_class.followers.add(to_add)
            else:
                messages.error(request, "CRN not found!")

        return render( request, "classes.html", {"my_context" : my_context} )
        
    else:
        messages.error( request, 'You must login to access class view.' )
        return redirect( reverse( "home" ), {} ) 

def about_view(request, *args, **kwargs): 
    my_context = {
        "akey":"This is about this site",
        "anumber": 100,
        "alist" : [ 123, 456, 789],
    }
    return render(request,"about.html", my_context)

