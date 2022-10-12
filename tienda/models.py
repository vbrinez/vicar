from asyncio.windows_events import NULL
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from pickle import TRUE

# Create your models here.

class producto (models.Model):
    codigo=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    mini_descripcion=models.CharField(max_length=60, null=TRUE)
    descripcion=models.TextField(null=TRUE)
    ruta_img=models.CharField(max_length=255,null=TRUE)
    categoria=models.CharField(max_length=50)
    fecha=models.DateTimeField(auto_now=TRUE,null=TRUE)
    precio=models.IntegerField()
    stock=models.IntegerField()
    status=models.IntegerField()

