from django.db import models
import datetime
import random

from django.db import models
from django.utils import timezone
from django.db.models import F, Sum, Count

class Categories(models.Model):
    name = models.CharField(max_length=50, default="")
    desc = models.TextField(max_length=400, default="")
    def __str__(self):
        return str(self.id) + ":" + self.name

class TypeList(models.Model): #ประเภทการแข่ง
    nameType = models.CharField(max_length=50, default="")
    gender = models.TextField(max_length=400, default="")
    def __str__(self):
        return self.nameType + ":" + self.gender

class Director(models.Model): #กรรมการ
    name = models.CharField(max_length=50, default="")
    gender = models.TextField(max_length=40, default="")
    birthdate = models.DateField(default=None)
    tel = models.CharField(max_length=10, default="")
    address = models.CharField(max_length=400, default="")
    def __str__(self):
        return self.name + ":" + self.gender + ":" + str(self.birthdate) + ":" + self.tel + ":" + self.address



class AgeCategory(models.Model): #ช่วงอายุ
    name = models.CharField(max_length=50, default="")
    desc = models.TextField(max_length=400, default="")

    def __str__(self):
        return self.name + ":" + self.desc

class Season(models.Model): #ฤดูกาล
    name = models.CharField(max_length=50, default="")
    desc = models.TextField(max_length=400, default="")

    def __str__(self):
        return self.name + ":" + self.desc


