from asyncio.windows_events import NULL
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from pickle import TRUE

# Create your models here.

class publicaciones(models.Model):
    mini_descripcion=models.CharField(max_length=60, null=TRUE)
    descripcion=models.TextField(null=TRUE)
    categoria=models.CharField(max_length=50)
    codigo_producto=models.CharField(max_length=50)
    nombre_producto=models.CharField(max_length=50)
    precio=models.IntegerField()
    stock=models.IntegerField()
    status=models.IntegerField()
    fecha=models.DateTimeField(auto_now=TRUE,null=TRUE)
    id_vendedor=models.IntegerField()

class imagenes(models.Model):
    ruta_img=models.CharField(max_length=255,null=TRUE)
    id_publicacion=models.IntegerField()

