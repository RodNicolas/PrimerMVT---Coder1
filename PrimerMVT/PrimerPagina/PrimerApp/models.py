
from django.db import models

# Create your models here.

class Familia(models.Model):
    
    nombre = models.CharField(max_length=50)
    
    

class Nico(models.Model):
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.CharField(max_length=50, default="26")
    fecha_nacimiento = models.DateField()
    
class Flor(models.Model):
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.CharField(max_length=50, default="24")
    fecha_nacimiento = models.DateField()
    
class Paco(models.Model):
    
    nombre = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()