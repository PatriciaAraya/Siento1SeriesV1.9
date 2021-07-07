from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import EmailField

# Create your models here.

class Plataforma(models.Model):
    idPlataforma = models.AutoField(primary_key=True, verbose_name="Id Plataforma")
    nombrePlataforma = models.CharField(max_length=80, blank=False, null=False, verbose_name="Nombre de la Plataforma")
 
    def __str__(self):
        return self.nombrePlataforma
 
class Series(models.Model):
    nombre = models.CharField(max_length=80, primary_key=True, blank=False, null=False, verbose_name="Nombre de la Serie")
    genero = models.CharField(max_length=80, null=True, blank=True, verbose_name="Género")
    imagen = models.ImageField(upload_to="images/", default="sinfoto.jpg", null=False, blank=False, verbose_name="Imagen")
    sinopsis = models.CharField(null=True, blank=True, max_length=1000, verbose_name="Sinopsis")
    desarrollo=models.CharField(null=True, blank=True,max_length=1000,verbose_name="Desarrollo")
    controversias=models.CharField(null=True, blank=True, max_length=1000,verbose_name="Controversia")    
    plataforma = models.ForeignKey(Plataforma, on_delete=models.DO_NOTHING)
    
    
 
    def __str__(self):
        return self.nombre



    
