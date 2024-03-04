from django import forms
from django.forms import ModelForm
from.models import user_data
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
    
class Register_user(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1','password2' ]
    
    
    