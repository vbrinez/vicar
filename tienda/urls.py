
from django.urls import path
from tienda.views import agregar_publicacion, verproductos, add_publicacion, add_imagenes, agregar_imagenes, subida

urlpatterns = [
                path('subida/',subida),    
                path('verproducto/',verproductos),
                path('addproducto/',add_publicacion),
                path('agregar_publicacion/',agregar_publicacion),
                path('addimagenes/',add_imagenes),
                path('agregar_imagenes/',agregar_imagenes),

]