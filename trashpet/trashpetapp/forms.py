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
class GamemakerForm(forms.Form):
    item_name = forms.CharField(max_length=50, label='Item Name:', widget=forms.TextInput(attrs={'placeholder': 'Enter item name'}))
    item_type = forms.CharField(max_length=20, label='Item Type:', widget=forms.TextInput(attrs={'placeholder': 'Enter item type'}))
    item_code = forms.CharField(max_length=20, label='Unlock Code:', widget=forms.TextInput(attrs={'placeholder': 'Enter unlock code for players to use'}))
    item_price = forms.IntegerField(label='Price:')
    item_link = forms.CharField(max_length=50, label='Item Link:', widget=forms.TextInput(attrs={'placeholder': 'Enter item filename'}))
   