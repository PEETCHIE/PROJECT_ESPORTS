from django.shortcuts import render,redirect

from django.shortcuts import render,redirect,get_object_or_404, HttpResponse
from django.db.models import Q
from APP_ESPORTS.forms import *
from APP_ESPORTS.models import *
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# def chkPermission(request):
#     if 'userStatus' in request.session:
#         userStatus = request.session['userStatus']
#         if userStatus == 'customer':
#             messages.add_message(request, messages.WARNING, "ท่านกำลังเข้าใช้ในส่วนที่ไม่ได้รับอนุญาต!!!")
#             return False
#         else:
#             return True
#     else:
#         if Employees.objects.count() != 0:
#             messages.add_message(request, messages.WARNING, "ท่านกำลังเข้าใช้ในส่วนที่ไม่ได้รับอนุญาต!!!")
#             return False
#         else:
#             return True


#AGE CATE GORY
def ageCategory(request):
    age = AgeCategory.objects.all().order_by()
    context = {'age':age}
    return render(request,"ageCategory.html",context)

def newAgeCategory(request):
    if request.method == 'POST':
        form = AgeCategoryForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ageCategory')
        else:
            context = {'form': form}
            return render(request, 'CRUD/AgeCategoryNew.html', context)
    else:
        form = AgeCategoryForm()
        context = {'form': form}
        return render(request, 'CRUD/AgeCategoryNew.html', context)

def updateAgeCategory(request, id):
    agecategory = get_object_or_404(AgeCategory, id=id)
    form = AgeCategoryForm(data=request.POST or None, instance=agecategory)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('ageCategory')
        else:
            context = {'form': form}
            return render(request, 'CRUD/DirectorUpdate.html')
    else:
        context = {'form': form}
        return render(request, 'CRUD/DirectorUpdate.html', context)

def deleteAgeCategory(request, id):
    agecategory = get_object_or_404(AgeCategory, id=id)
    form = AgeCategoryForm(data=request.POST or None, instance=agecategory)
    if request.method == 'POST':
        agecategory.delete()
        return redirect('ageCategory')
    else:
        form.deleteForm()
        context = {'form': form, 'agecategory': agecategory}
        return render(request, 'CRUD/RaceTypeDelete.html', context)



#SEASON
def season(request):
    sea = Season.objects.all().order_by()
    context = {'sea':sea}
    return render(request,"season.html",context)
def newSeason(request):
    if request.method == 'POST':
        form = SeasonForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('season')
        else:
            context = {'form': form}
            return render(request, 'CRUD/SeasonNew.html', context)
    else:
        form = AgeCategoryForm()
        context = {'form': form}
        return render(request, 'CRUD/SeasonNew.html', context)

def updateSeason(request, id):
    seasons = get_object_or_404(Season, id=id)
    form = AgeCategoryForm(data=request.POST or None, instance=seasons)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('season')
        else:
            context = {'form': form}
            return render(request, 'CRUD/SeasonUpdate.html')
    else:
        context = {'form': form}
        return render(request, 'CRUD/SeasonUpdate.html', context)

def deleteSeasaon(request, id):
    seasons = get_object_or_404(Season, id=id)
    form = AgeCategoryForm(data=request.POST or None, instance=seasons)
    if request.method == 'POST':
        seasons.delete()
        return redirect('season')
    else:
        form.deleteForm()
        context = {'form': form, 'season': seasons}
        return render(request, 'CRUD/SeasonDelete.html', context)

def base(request):
    return render(request,"base.html")

#DIRECTOR กรรมการ
def director(request):
    direc = Director.objects.all().order_by()
    context = {'direc':direc}
    return render(request,"director.html",context)

def newDirector(request):
    if request.method == 'POST':
        form = DirectorForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('director')
        else:
            context = {'form': form}
            return render(request, 'CRUD/DirectorNew.html', context)
    else:
        form = DirectorForm()
        context = {'form': form}
        return render(request, 'CRUD/DirectorNew.html', context)

def updateDirector(request, id):
    director = get_object_or_404(Director, id=id)
    form = DirectorForm(data=request.POST or None, instance=director)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('director')
        else:
            context = {'form': form}
            return render(request, 'CRUD/DirectorUpdate.html')
    else:
        context = {'form': form}
        return render(request, 'CRUD/DirectorUpdate.html', context)

def deleteDirector(request, id):
    director = get_object_or_404(Director, id=id)
    form = DirectorForm(data=request.POST or None, instance=director)
    if request.method == 'POST':
        director.delete()
        return redirect('director')
    else:
        form.deleteForm()
        context = {'form': form, 'typelist': director}
        return render(request, 'CRUD/RaceTypeDelete.html', context)
#TYPE
def typeList(request):
    typelist = TypeList.objects.all().order_by()
    context = {'raceType': typelist}
    return render(request,"raceType.html",context)
def newRaceType(request):
    if request.method == 'POST':
        form = RaceTypeForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('raceType')
        else:
            context = {'form': form}
            return render(request, 'CRUD/RaceTypeNew.html', context)
    else:
        form = RaceTypeForm()
        context = {'form': form}
        return render(request, 'CRUD/RaceTypeNew.html', context)

def updateRaceType(request, id):
    typelist = get_object_or_404(TypeList, id=id)
    form = RaceTypeForm(data=request.POST or None, instance=typelist)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('raceType')
        else:
            context = {'form': form}
            return render(request, 'CRUD/RaceTypeUpdate.html')
    else:
        context = {'form': form}
        return render(request, 'CRUD/RaceTypeUpdate.html', context)

def deleteRaceType(request, id):
    typelist = get_object_or_404(TypeList, id=id)
    form = RaceTypeForm(data=request.POST or None, instance=typelist)
    if request.method == 'POST':
        typelist.delete()
        return redirect('raceType')
    else:
        form.deleteForm()
        context = {'form': form, 'typelist': typelist}
        return render(request, 'CRUD/RaceTypeDelete.html', context)


