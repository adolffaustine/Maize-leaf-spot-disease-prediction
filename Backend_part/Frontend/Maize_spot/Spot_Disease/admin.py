from django.contrib import admin
from .models import Maize
# Register your models here.



class MaizeModel(admin.ModelAdmin):
    list_filter = ('maize_image','disease_name')
    list_display = ('maize_image','disease_name')

admin.site.register(Maize ,MaizeModel)