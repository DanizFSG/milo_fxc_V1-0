from django.urls import path
from . import views

urlpatterns =[
    
    path("Tikets/", views.Tikets_Garantias, name='Tikets')
    
]