from django.urls import path
from .views import home,index, registrarUsuario, login, login_app

urlpatterns= [
    path('home/<int:id>', home,name="home"),
    path('index', index,name="index"),
    path('registrarUsuario',registrarUsuario,name="registrarUsuario"),
    path('', login,name="login"),
    path('login_app/',login_app,name="login_app"),
]