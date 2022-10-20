import math
from itertools import count
from urllib import request
from django.shortcuts import render,redirect
from django.db.models import Q
from tienda.models import publicaciones, imagenes
from django.contrib.auth.decorators import login_required
# Create your views here.

def verproductos(request):
    todaspublicaciones=publicaciones.objects.all()
    productos=publicaciones.objects.all().count()
    productosXfilas=4
    sucesion=set()
    if (productos>0):
        cantfilas=math.ceil(productos/productosXfilas)
        cantfilas=cantfilas*productosXfilas
        for i in range(cantfilas):
            if ((cantfilas-i)%productosXfilas==0):
                sucesion={i}
    else:
        sucesion={0}
        productos=0
    print (productos)
    return render(request, "productos.html", {'nombre':'Victor','nombre_completo':'Victor Briñez','id_usuario':'1','publicaciones':todaspublicaciones,'filas':sucesion,'productos':productos})

@login_required(login_url="/login")
def add_publicacion(request):
    return render(request, "addproducto.html")

@login_required(login_url="/login")
def subida(request):
    return render(request, "subida.html")
@login_required(login_url="/login")
def add_imagenes(request):
    return render(request, "addimagenes.html")

@login_required(login_url="/login")
def agregar_publicacion(request):
    ultimo = publicaciones.objects.all().count()
    if (ultimo==0) or (ultimo==''):
        ultimo = 1
    else:
        ultimo = ultimo + 1
    codigo_producto=request.POST['codigo_producto']
    nombre_producto=request.POST['nombre_producto']
    mini_descripcion=request.POST['minidescrip']
    descripcion=request.POST['descrip']
    categoria=request.POST['categoria']
    precio=request.POST['precio']
    stock=request.POST['stock']
    status=request.POST['status']
    id_vendedor=request.POST['vendedor']
    publicacion=publicaciones.objects.create(id_publicacion=ultimo,codigo_producto=codigo_producto,nombre_producto=nombre_producto,mini_descripcion=mini_descripcion,descripcion=descripcion,categoria=categoria,precio=precio,stock=stock,status=status,id_vendedor=id_vendedor)
    id_ultima_publicacion = publicaciones.objects.get(id_publicacion=ultimo)
    return render(request,"addimagenes.html",{'id':id_ultima_publicacion.id_publicacion,'nombre':id_ultima_publicacion.nombre_producto, 'codigo':id_ultima_publicacion.codigo_producto})

def agregar_imagenes(request):
    ultimo = imagenes.objects.all().count()
    if (ultimo==0) or (ultimo==''):
        ultimo = 1
    else:
        ultimo = ultimo + 1
    rutas_imagenes=request.POST['files']

    imagen=imagenes.objects.create(id_imagen=ultimo,imagen=rutas_imagenes,id_publicacion=1)
    return render(request,"home.html")

