from django.contrib import admin
from gpo.models import *

class MissionAdmin(admin.ModelAdmin):
    list_display = ('NomMission', 'DateDebut', 'DateFin', 'Description', 'Nigend')

class PersonnelAdmin(admin.ModelAdmin):
    list_display = ('Nigend', 'Nom', 'Prenom', 'Tel', 'Mail')

class MaterielAdmin(admin.ModelAdmin):
    list_display = ('Materiel', 'ChampControle')

admin.site.register(Mission, MissionAdmin)
admin.site.register(Personnel, PersonnelAdmin)
admin.site.register(Materiel, MaterielAdmin)

