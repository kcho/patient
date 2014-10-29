from django.db import models
from django.contrib import admin

# Create your models here.

class Patient(models.Model):
    hospitalID = models.CharField(max_length=8)
    initial = models.CharField(max_length=5)
    group = models.CharField(max_length=5)
    folderName = models.CharField(max_length=10)
    age = models.IntegerField()
    t1Number = models.IntegerField()
    dtiNumber = models.IntegerField()
    restNumber = models.IntegerField()
    dkiNumber = models.IntegerField()
    backupLocation = models.CharField(max_length=60)
    scanDate = models.DateField()
    #image = models.IntegerField()

class PatientAdmin(admin.ModelAdmin):
    list_display = ["hospitalID","initial","group","folderName","age","t1Number","dtiNumber","restNumber","dkiNumber","backupLocation","scanDate"]
    search_fields = ["hospitalID"]
