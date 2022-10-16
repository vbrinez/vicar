from django.contrib import admin
from django.urls import path,include
from tienda.views import verproductos
from blog.views import home,ver,mod,add,registrarUsuario,editarUsuario, eliminarUsuario, modificarUsuario, addpublicacion,addcategoria,registrarCategoria,registrarPublicacion, readme, perfil, articulo, login

urlpatterns = [
    path('readme',readme),
    path('home',home),
    path('ver/',ver),
    path('mod',mod),
    path('add/',add),
    path('registrarUsuario/', registrarUsuario),
    path('editarUsuario/<id>/', editarUsuario),
    path('modificarUsuario/', modificarUsuario),
    path('eliminarUsuario/<id>/', eliminarUsuario),
    path('addpublicacion', addpublicacion),
    path('addcategoria', addcategoria),
    path('registrarCategoria/', registrarCategoria),
    path('registrarPublicacion/', registrarPublicacion),
    path('perfil/<id>/', perfil),
    path('articulo/<id>/', articulo),
    
]
