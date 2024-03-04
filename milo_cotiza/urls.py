from django.urls import path
from . import views

urlpatterns = [

    path("", views.Inicio, name='Inicio'),
    path("login/", views.user_login, name='login'),
    path("logout/", views.user_logout, name='logout'),
    path("registrar/", views.user_Register, name='register'),
    path("cotizacion/", views.Milo_cotiza, name='Milo_cotiza'),
    

]