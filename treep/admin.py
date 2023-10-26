from django.contrib import admin
from .models import *

# Register your models here.

class Apagar(admin.ModelAdmin):
    def delete_model(self, request, obj):
        obj.img.delete(save=True)
        obj.delete()
         

    def delete_queryset(self, request, queryset):

        for obj in queryset.all():
            obj.img.delete(save=True)
        queryset.delete()

admin.site.register(Natureza,Apagar)
admin.site.register(Gastronomia,Apagar)
admin.site.register(Praia,Apagar)
admin.site.register(Cultura,Apagar)

#admin.site.register(Roteiro)

from django.db import models
from django.contrib import admin
from django.forms import CheckboxSelectMultiple

class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
admin.site.register(Roteiro,MyModelAdmin)
