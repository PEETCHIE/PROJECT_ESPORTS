from django.shortcuts import render,redirect

from APP_ESPORTS.forms import *
from APP_ESPORTS.models import *

def typeList(request):
    typelist = TypeList.objects.all().order_by()
    context = {'raceType': typelist}
    return render(request,"raceType.html",context)

def director(request):
    direc = Director.objects.all().order_by()
    context = {'direc':direc}
    return render(request,"director.html",context)

def ageCategory(request):
    age = AgeCategory.objects.all().order_by()
    context = {'age':age}
    return render(request,"ageCategory.html",context)

def season(request):
    sea = Season.objects.all().order_by()
    context = {'sea':sea}
    return render(request,"season.html",context)

def base(request):
    return render(request,"base.html")

def newRaceType(request):
    return render(request,"CRUD/newRaceType.html")






