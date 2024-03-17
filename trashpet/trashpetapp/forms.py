from typing import Any
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Form to create new user
class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

#Form to login
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))

#Form to rename pet
class RenamePetForm(forms.Form):
    pet_name = forms.CharField(max_length=30, label='', widget=forms.TextInput(attrs={'placeholder': 'Enter new pet name'})) # 30???

#Form for unlock codes
class CodeForm(forms.Form):
    code = forms.CharField(max_length=30, label='', widget=forms.TextInput(attrs={'placeholder': 'Enter code here'}))

#Gamemaker form to add shop items