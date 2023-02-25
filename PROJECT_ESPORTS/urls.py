"""PROJECT_ESPORTS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from APP_ESPORTS import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.base, name='base'),
    #DIRECTOR
    path('director',views.director,name='director'),
    path('newDirector',views.newDirector,name='newDirector'),
    path('<id>/updateDirector',views.updateDirector,name='updateDirector'),
    path('<id>/deleteDirector',views.deleteDirector,name='deleteDirector'),

    #AGE CATEGORY
    path('ageCategory',views.ageCategory, name='ageCategory'),
    path('newAgeCategory', views.newAgeCategory, name='newAgeCategory'),
    path('<id>/updateAgeCategory', views.updateAgeCategory, name='updateAgeCategory'),
    path('<id>/deleteAgeCategory', views.deleteAgeCategory, name='deleteAgeCategory'),

    path('season', views.season,name='season'),
    path('newSeason', views.newSeason, name='newSeason'),
    path('<id>/updateSeason', views.updateSeason, name='updateSeason'),
    path('<id>/deleteSeason', views.deleteSeasaon, name='deleteSeason'),
    #TYPE
    path('raceType',views.typeList, name='raceType'),
    path('newRaceType',views.newRaceType,name='newRaceType'),
    path('<id>/updateRaceType', views.updateRaceType, name='updateRaceType'),
    path('<id>/deleteRaceType', views.deleteRaceType, name='deleteRaceType'),
]
