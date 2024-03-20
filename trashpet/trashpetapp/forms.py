from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RenamePetForm(forms.Form):
    pet_name = forms.CharField(max_length=30, label='', widget=forms.TextInput(attrs={'placeholder': 'Enter new pet name'})) # 30???

class CodeForm(forms.Form):
    code = forms.CharField(max_length=30, label='', widget=forms.TextInput(attrs={'placeholder': 'Enter code here'}))

#Gamemaker form to add shop items
class GamemakerForm(forms.Form):
    item_name = forms.CharField(max_length=50, label='Item Name:', widget=forms.TextInput(attrs={'placeholder': 'Enter item name'}))
    item_type = forms.CharField(max_length=20, label='Item Type:', widget=forms.TextInput(attrs={'placeholder': 'Enter item type'}))
    item_code = forms.CharField(max_length=20, label='Unlock Code:', widget=forms.TextInput(attrs={'placeholder': 'Enter unlock code'}))
    item_price = forms.IntegerField(label='Price:')
    item_link = forms.CharField(max_lenth=50, label="Image Name:", widget=forms.TextInput(attrs={'placeholder': 'Enter item url'}))
    gamemaker_form = forms.BooleanField(widget=forms.HiddenInput, initial=True)
   
#Gamemaker form to add money codesß
class LeavesCodeForm(forms.Form):
    code = forms.CharField(max_length=30, label='Unlock Code:', widget=forms.TextInput(attrs={'placeholder': 'Enter code here'}))
    leaves = forms.IntegerField(label='Reward:')
    leavescode_form = forms.BooleanField(widget=forms.HiddenInput, initial=True)