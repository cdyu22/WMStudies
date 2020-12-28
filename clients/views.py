from django.shortcuts import render

from .models import Person

def person_detail_view(request):
    obj = Person.objects.get(id=1)
    # context = {
    #     'first_name' : obj.first_name,
    #     'last_name'  : obj.last_name,
    # }
    context = {
        'object' : obj
    }
    return render(request,"product/detail.html",context)
