from django.shortcuts import render
#Importamos la vista genérica FormView
from django.views.generic.edit import FormView
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
#Importamos el formulario de autenticación de django
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

# Create your views here.
def Login(request):
    #Establecemos la plantilla a utilizar
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')

            user = authenticate(username = user, password = pwd)

            if user is not None:
                login(request, user)
                return render(request, 'home.html')
            else:
                return render(request, 'error.html', {'form':form})
        else:
            return render(request, 'error2.html', {'form':form})
   
    form = AuthenticationForm()
    return render(request, 'login.html' , {'form': form})