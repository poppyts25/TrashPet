from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm
from .models import UserProfile

def index(request):
    return render(request, "trashpetapp/index.html")

# Create your views here.
def home(request):
    #template = loader.get_template("trashpetapp/home.html")
    return render(request, "trashpetapp/home.html")


def shop(request):
    return HttpResponse("Shop")

def map(request):
    return HttpResponse("map")

def camera(request):
    return HttpResponse("camera")

def profile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    username = user.username
    leaves = profile.leaves

    return render(request, "trashpetapp/profile.html", {"username": username, "leaves": leaves})



def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'trashpetapp/signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'trashpetapp/login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')