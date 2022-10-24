import math
from urllib import request
from django.shortcuts import render,redirect
from .models import user, Publicaciones,Categoria
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.
@login_required(login_url="/login")
def home(request):
    buscar= request.GET.get("busqueda")
    if buscar:
        publicaciones_cuantos = Publicaciones.objects.filter(
            Q(titulo__icontains= buscar) |
            Q(resumen__icontains = buscar)
            ).distinct().count()
        if publicaciones_cuantos>=1:
            publicaciones = Publicaciones.objects.filter(
            Q(titulo__icontains= buscar) |
            Q(resumen__icontains = buscar)
            ).distinct()
        else:
            publicaciones=Publicaciones.objects.all()   
            articulos=publicaciones.objects.all().count()
            articulosXfilas=3
            cantfilas=math.ceil(articulos/articulosXfilas)
            cantfilas=cantfilas*articulosXfilas
            sucesion=set()
            for i in range(cantfilas):
                if ((cantfilas-i)%articulosXfilas==0):
                    sucesion={i}
    else:
        articulos=Publicaciones.objects.all()
        cant_articulos=Publicaciones.objects.all().count()
        articulosXfilas=3
        cantfilas=math.ceil(cant_articulos/articulosXfilas)
        cantfilas=cantfilas*articulosXfilas
        sucesion=set()
        for i in range(cantfilas):
            if ((cantfilas-i)%articulosXfilas==0):
                sucesion={i}
    usuarios=user.objects.all()
    categoria=Categoria.objects.all()
    return render(request,"home.html",{"publicaciones":articulos,"usuarios":usuarios,"categoria":categoria,"sucesion":sucesion})

def landing(request):
    buscar= request.GET.get("busqueda")
    if buscar:
        publicaciones_cuantos = Publicaciones.objects.filter(
            Q(titulo__icontains= buscar) |
            Q(resumen__icontains = buscar)
            ).distinct().count()
        if publicaciones_cuantos>=1:
            publicaciones = Publicaciones.objects.filter(
            Q(titulo__icontains= buscar) |
            Q(resumen__icontains = buscar)
            ).distinct()
        else:
            publicaciones=Publicaciones.objects.all()   
    else:
        publicaciones=Publicaciones.objects.all()
    usuarios=user.objects.all()
    categoria=Categoria.objects.all()
    return render(request,"landing.html",{"publicaciones":publicaciones,"usuarios":usuarios,"categoria":categoria})

@login_required(login_url="/login")
def ver(request):
    usuarios=user.objects.all()
    return render(request, "ver.html", {"usuarios":usuarios})

@login_required(login_url="/login")
def mod(request):
    usuario=user.objects.all()
    return render(request,"mod.html", {"usuarios":usuario})

@login_required(login_url="/login")
def add(request):
    return render(request,"add.html")

@login_required(login_url="/login")
def addcategoria(request):
    return render(request,"addcategoria.html")

def readme(request):
    return render(request,"readme.html")

@login_required(login_url="/login")
def addpublicacion(request):
    usuarios=user.objects.all()
    categorias=Categoria.objects.all()
    return render(request, "addpublicacion.html", {"usuarios":usuarios,"categorias":categorias})

@login_required(login_url="/login")
def registrarPublicacion(request):
    titulo=request.POST['titulo']
    resumen=request.POST['resumen']
    articulo=request.POST['articulo']
    id_categoria=request.POST['id_categoria']
    id_usuario=request.POST['id_usuario']
    publicacion=Publicaciones.objects.create(titulo=titulo,resumen=resumen,contenido=articulo,id_categoria=id_categoria,id_usuario=id_usuario)
    return redirect('/blog/home')

@login_required(login_url="/login")
def registrarUsuario(request):
    nombre=request.POST['nombre']
    apellido=request.POST['apellido']
    correo=request.POST['correo']
    password=request.POST['pw1']
    telefono=request.POST['telefono']
    tipo=request.POST['tipo_usuario']
    usuario=user.objects.create(username=nombre,first_name=nombre,last_name=apellido,email=correo,password=password)
    return redirect('/blog/ver')

@login_required(login_url="/login")
def registrarCategoria(request):
    nombre=request.POST['nombre']
    categoria=Categoria.objects.create(nombre=nombre)
    return redirect('/blog/addpublicacion')

@login_required(login_url="/login")
def eliminarUsuario(request, id):
    usuario=user.objects.get(id_usuario=id)
    user.delete()
    return redirect('/blog/ver')

@login_required(login_url="/login")
def editarUsuario(request, id):
    usuario=user.objects.get(id=id)
    return render(request, "editar.html", {'usuario':usuario})

@login_required(login_url="/login")
def perfil(request, id):
    usuario=user.objects.get(id_usuario=id)
    return render(request, "perfil.html", {'usuario':usuario})

@login_required(login_url="/login")
def articulo(request, id):
    publicacion=Publicaciones.objects.get(id_publicaciones=id)
    usuarios=user.objects.all()
    categoria=Categoria.objects.all()
    return render(request, "post.html", {'publicaciones':publicacion,"usuarios":usuarios,"categorias":categoria})

@login_required(login_url="/login")
def modificarUsuario(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    apellido=request.POST['apellido']
    telefono=request.POST['telefono']
    correo=request.POST['correo']
    tipo=request.POST['tipo_usuario']
    usuario=user.objects.get(id_usuario=id)
    user.nombre=nombre
    user.apellido=apellido
    user.correo=correo
    user.telefono=telefono
    user.tipo=tipo
    user.save()
    return redirect('/blog/ver')
