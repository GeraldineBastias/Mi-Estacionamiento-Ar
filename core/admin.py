from django.contrib import admin

from core.models import Estacionamiento, Tipo_Estacionamiento, Tipo_Usuario, Usuario

# Register your models here.
admin.site.register(Tipo_Usuario)
admin.site.register(Usuario)
admin.site.register(Tipo_Estacionamiento)
admin.site.register(Estacionamiento)