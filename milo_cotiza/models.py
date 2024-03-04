from django.db import models

# Create your models here.

class user_data(models.Model):
    username = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    celular = models.CharField(max_length=100)
    nit = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
class Unit(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
