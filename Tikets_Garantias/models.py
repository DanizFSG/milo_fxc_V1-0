from django.db import models

# Create your models here.

class Models_Tickets(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.CharField(max_length=100),
    correo_ticket = models.EmailField(max_length=100),
    empresa = models.CharField(max_length=100),
    refereencia = models.CharField(max_length=100),
    serial = models.CharField(max_length=100),
    marca = models.CharField(max_length=100),
    garantia = models.CharField(max_length=100),
    fecha_ingreso = models.DateField(auto_now_add=True),
    fecha_salida = models.DateField(auto_now_add=True),
    foto_equipo = models.ImageField(upload_to=''),
    foto_1 = models.ImageField(upload_to=''),
    foto_2 = models.ImageField(upload_to=''),