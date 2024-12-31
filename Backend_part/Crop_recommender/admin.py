from django.contrib import admin
from .models import Crop

# Register your models here.

class DataAdmin(admin.ModelAdmin):
    list_display = ('Area','Taken_at', 'Nitrogen', 'Phosphorus', 'Potassium', 'Temperature', 'Humidity', 'Soil_pH', 'Rainfall', 'Crop_supported', 'Action')

admin.site.register(Crop, DataAdmin)