from django.contrib import admin
from django.urls import path,include
from seguridad.views import Login 
urlpatterns = [
    path('', Login)
    
]