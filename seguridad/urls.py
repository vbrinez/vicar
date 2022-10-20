from django.contrib import admin
from django.urls import path,include
from seguridad.views import Login,logout
urlpatterns = [
    path('', Login),
    path('logout/', logout),
    path( "accounts/",include("django.contrib.auth.urls")),   # nuevo 
]
    