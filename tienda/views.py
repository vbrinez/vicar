import math
from itertools import count
from urllib import request
from django.shortcuts import render,redirect
from django.db.models import Q
from tienda.models import publicaciones
# Create your views here.

def verproductos(request):
    todaspublicaciones=publicaciones.objects.all()
    productos=publicaciones.objects.all().count()
    productosXfilas=4
    cantfilas=math.ceil(productos/productosXfilas)
    cantfilas=cantfilas*productosXfilas
    sucesion=set()
    for i in range(cantfilas):
        if ((cantfilas-i)%productosXfilas==0):
            sucesion={i}
    return render(request, "productos.html", {'nombre':'Victor','nombre_completo':'Victor Briñez','id_usuario':'1','publicaciones':todaspublicaciones,'filas':sucesion,'productos':productos})
    
def add_publicacion(request):
    return render(request, "addproducto.html")

def agregar_publicacion(request):
    codigo_producto=request.POST['codigo_producto']
    nombre_producto=request.POST['nombre_producto']
    mini_descripcion=request.POST['minidescrip']
    descripcion=request.POST['descrip']
    categoria=request.POST['categoria']
    precio=request.POST['precio']
    stock=request.POST['stock']
    status=request.POST['status']
    id_vendedor=request.POST['vendedor']
    publicacion=publicaciones.objects.create(codigo_producto=codigo_producto,nombre_producto=nombre_producto,mini_descripcion=mini_descripcion,descripcion=descripcion,categoria=categoria,precio=precio,stock=stock,status=status,id_vendedor=id_vendedor)
    return redirect('/tienda/verproducto')




