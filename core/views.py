from django.shortcuts import render, redirect
from .models import Usuario, Tipo_Estacionamiento, Tipo_Usuario, Estacionamiento
import base64
# Create your views here.

def home(request,id):
    sesion = Usuario.objects.get(idUsuario = id)

    contexto = {
        "sesion":sesion
    }
    return render(request, 'core/home.html',contexto)


def index(request):
    return render(request, 'core/index.html')


def registrarUsuario(request):

    rut1     = request.POST['rut']
    dv1      = request.POST['dv']
    uname1   = request.POST['uname']
    name1    = request.POST['name']
    apat1    = request.POST['apat']
    amat1    = request.POST['amat']
    corre1   = request.POST['corre']
    pass1    = request.POST['pass']
    tele1    = request.POST['tele']
    try:
        c = Usuario.objects.get(correo = corre1)
        c1 = False
    except Usuario.DoesNotExist:
        c1 = True      
    try:
        x = Usuario.objects.get(username = uname1)
        x1 = False
    except Usuario.DoesNotExist:
        x1 = True
    if c1 == True and x1 == True:

        idTip = Tipo_Usuario.objects.get(tipo = "Cliente")

        Usuario.objects.create(run = rut1, dv = dv1, 
            nombre = name1, apellidopaterno = apat1, 
            apellidomaterno = amat1, correo = corre1, 
            username = uname1, password = pass1, 
            celular = tele1, idTipo = idTip)

        
        # messages.success(request, 'Cuenta registrada')
        return redirect ('home')
    else:
        # messages.error(request, 'El nombre de usuario o correo ya estan ocupados')
        return redirect ('home')

def login(request):
    return render(request, 'core/login.html')

def login_app(request):
    co = request.POST['corre']
    ps = request.POST['pass']

    try:
        x = Usuario.objects.get(username = co, password = ps) 
        sesion = str(ps)
        return redirect ('home',x.idUsuario)
 
    except Usuario.DoesNotExist:
        # messages.error(request, 'Usuario y/o clave incorrecta')
        return redirect ('login')
