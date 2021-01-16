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
        else:
            messages.error(request, 'Invalid. Need unique username. Phone number should be only 10 numbers. Only supports US phones.')
            return redirect( reverse( "register"))

def logout_view( request, *args, **kwargs ):
    logout( request )
    return redirect( reverse( "home" ) )


def classes_view(request,*args, **kwargs):
    if not request.user.is_authenticated:
        messages.error( request, 'You must login to access class view.' )
        return redirect( reverse( "home" )) 

    if request.method == "POST":
        CRN_Taker = request.POST.get( 'CRN_Taker' )
        if CRN_Taker == "":
            pass
        elif Course.objects.filter(CRN=CRN_Taker).exists():
            specified_class = Course.objects.get(CRN=CRN_Taker)
            to_add = User.objects.get(username=request.user)
            specified_class.followers.add(to_add)
        else:
            messages.error(request, "Added CRN not found!")

        CRN_Remover = request.POST.get( 'CRN_Remover' )
        if CRN_Remover == "":
            pass
        elif Course.objects.filter(CRN=CRN_Remover).exists():
            specified_class = Course.objects.get(CRN=CRN_Remover)
            to_remove = User.objects.get(username=request.user)
            if to_remove.course_set.filter(CRN=CRN_Remover).exists():
                specified_class.followers.remove(to_remove)
            else:
                messages.error(request, "User is not following " + CRN_Remover)
            
        else:
            messages.error(request, "Removed CRN not found!")     
        

    my_context = {}
    try: 
        curr_user = User.objects.get(username=request.user)
        for object in curr_user.course_set.all():
            my_context[ object.CRN ] =  [ object.section, object.course_name, object.status ]
        
    except AttributeError as e:
        print("User doesn't have any courses YET")
        print(e)
    except Exception as e:
        print("EXCEPTION!")
        print(e)

    return render( request, "classes.html", {"my_context" : my_context} )
    
   

def phone_change_view(request,*args, **kwargs):
    if not request.user.is_authenticated:
        messages.error( request, 'You must login to change phone number.' )
        return redirect( reverse( "home" ), {} ) 

    if request.method == "POST":
        phone_number1 = request.POST.get('Phone_Taker')
        phone_number2 = request.POST.get('Phone_Validate')
        if phone_number1 == phone_number2 and len(phone_number1) == 10:
            messages.error(request,"Phone number is valid")
            print("PHONE IS VALID")
            curr_user = User.objects.get(username=request.user)
            curr_user.phone_number = phone_number1
            curr_user.save()
        elif phone_number1 != phone_number2:
            messages.error(request, "Phone isn't valid")    
            print("phone isn't valid")
            print(phone_number1)
            print(phone_number2)

    return render(request,"phone_change.html")

def about_view(request, *args, **kwargs): 
    my_context = {
        "akey":"This is about this site",
        "anumber": 100,
        "alist" : [ 123, 456, 789],
    }
    return render(request,"about.html", my_context)

