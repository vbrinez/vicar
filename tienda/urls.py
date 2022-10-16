
from django.urls import path
from tienda.views import agregar_publicacion, verproductos, add_publicacion

urlpatterns = [
                path('verproducto/',verproductos),
                path('addproducto/',add_publicacion),
                path('agregar_publicacion/',agregar_publicacion),

]