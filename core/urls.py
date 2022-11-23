from django.urls import path
from .views import home,index, registrarUsuario

urlpatterns= [
    path('', home,name="home"),
    path('index', index,name="index"),
    path('registrarUsuario',registrarUsuario,name="registrarUsuario"),
]