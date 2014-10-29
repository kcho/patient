from django.contrib import admin

# Register your models here.
from mrCheck.models import *

admin.site.register(Patient, PatientAdmin)
