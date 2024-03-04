
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import Register_user
from .models import user_data



# Create your views here.


def Inicio(request):
    return render(request, ('Inicio.html'))
def Milo_cotiza(request):
    return render(request, ('Cotizacion_de_Materiales.html'))
def user_login(request):
    if request.method == 'GET':
            return render(request, 'login.html',{
        'form' : AuthenticationForm()
    } )
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is  None:
            return render(request, 'login.html',{
            'form' : AuthenticationForm(),
            'error' : 'Usuario o Contraseña Incorrecta'
        })
        else:
            login(request, user)
            return redirect('Inicio')
def user_Register(request):
    if request.method == 'GET':
        return render(request, 'registro_user.html',{
            'form' : Register_user()
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'], email=request.POST['email'], first_name=request.POST['first_name'], last_name=request.POST['last_name'])
                user.save()
                login(request, user)
                return render(request, 'registro_user.html', {
                        'form': Register_user(),
                        'error': 'registrado correctamente'
                    })  
            except IntegrityError:
                    return render(request, 'registro_user.html', {
                        'form': Register_user(),
                        'error': 'usurario ya existe'
                    })   
        return render(request, 'registro_user.html',{
            'form': Register_user(),
            'error': 'contrasena no coinciden'
            })       
def user_logout(request):
    logout(request)
    return redirect('Inicio')