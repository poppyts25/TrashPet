from typing import Any
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

    

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))

class RenamePetForm(forms.Form):
    pet_name = forms.CharField(max_length=30, label='', widget=forms.TextInput(attrs={'placeholder': 'Enter new pet name'})) # 30???

class CodeForm(forms.Form):
    code = forms.CharField(max_length=30, label='', widget=forms.TextInput())