from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length= 100)
    usuario = models.CharField("usuario",max_length=256)
    contraseña = models.CharField("contraseña", max_length=50)
    email = models.EmailField()
    def __str__(self):
        return self.usuario
    
class maquina(models.Model):   
    nombre = models.CharField('Nombre', max_length=100)
    
    def __str__(self):
        return self.nombre