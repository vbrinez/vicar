
from django.urls import path
from tienda.views import verproductos

urlpatterns = [
path('verproducto/',verproductos)
]