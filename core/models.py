from django.db import models

# Create your models here.

class Tipo_Usuario(models.Model):
    idTipo = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=60, null=False, blank=False)

    def __str__(self) :
            return self.tipo

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    run = models.IntegerField(null=False, blank=False)
    dv = models.CharField(max_length=1, blank=False, null=False)
    nombre = models.CharField(max_length=60, blank=False, null=False)
    apellidopaterno = models.CharField(max_length=60, blank=False, null=False)
    apellidomaterno = models.CharField(max_length=60, blank=False, null=False)
    correo = models.CharField(max_length=50, blank=False, null=False)
    celular = models.CharField(max_length=12, blank=False, null=False)
    username = models.CharField(max_length=60, null=False, blank=False)
    password = models.CharField(max_length=60, null=False, blank=False)
    idTipo = models.ForeignKey(Tipo_Usuario, on_delete= models.CASCADE, default=1)

    def __str__(self) :
            return self.username

class Tipo_Estacionamiento(models.Model):
    idTipoEsta = models.AutoField(primary_key=True)
    tipoEsta = models.CharField(max_length=60, null=False, blank=False)

    def __str__(self) :
            return self.tipoEsta

class Estacionamiento(models.Model):
    idEstacionamiento = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=100, blank=False, null=False)
    comuna = models.CharField(max_length=100, blank=False, null=False)
    cantidadVehiculo = models.IntegerField(null=False, blank=False)
    fecha = models.DateField(null=False, blank=False)
    hora = models.TimeField(null=False, blank=False)
    idUsuario = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    idTipoEsta = models.ForeignKey(Tipo_Estacionamiento, on_delete= models.CASCADE)

