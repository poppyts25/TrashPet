from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm, RenamePetForm, CodeForm
from .models import UserProfile, Accessory
from django.contrib.auth.decorators import login_required
import json

def index(request): 
    return render(request, "trashpetapp/index.html")

@login_required # automatically redirects to login page if not logged in
def home(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    petname = profile.pet_name
    return render(request, "trashpetapp/home.html", {"petname": petname})

@login_required
def shop(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    locked_list = profile.accessories
    try:
        locked_list = json.loads(locked_list)
    except:
        locked_list = {"Cap":False, "Crown":False, "Socks":False, "Bottle":True}

    accessories = Accessory.objects.all()

    return render(request, "trashpetapp/shop.html", {"accessories": accessories, "locked_list": locked_list})

@login_required
def map(request):
    return render(request, "trashpetapp/map.html")

@login_required
def garden(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    leaves = profile.leaves
    data = {"leaves":leaves} #view that handles ajax request
    return render(request, "trashpetapp/garden.html", data)

def update_leaves(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    leaves = profile.leaves
    if request.method == 'POST':
        # Get the new leaves value from the POST data
        new_leaves = request.POST.get('new_leaves')
        
        # Update the leaves value in your Django application
        profile.leaves=new_leaves
        profile.save()
        
        return JsonResponse({'new_leaves': new_leaves})
    else:
        # Handle other HTTP methods if necessary
        return render(request, 'trashpetapp/garden.html', {'leaves': 0})
            


@login_required
def camera(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    locked_list = profile.accessories
    try:
        locked_list = json.loads(locked_list)
    except:
        locked_list = {"Cap":False, "Crown":False, "Socks":False, "Bottle":True}
    accessories = Accessory.objects.all()
    

    if request.method == 'POST':
        form = CodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            
            for accessory in accessories:
                if accessory.code == code:
                    name = accessory.name
                    locked_list[name] = False
                    locked_list = json.dump(locked_list)
                    profile.accessories = locked_list
                    break
            return redirect("shop")
    else:
        form = CodeForm()
    return render(request, "trashpetapp/camera.html", {"form": form})

@login_required 
def profile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    username = user.username
    leaves = profile.leaves
    pet_name = profile.pet_name

    if request.method == 'POST':
        if 'delete_user' in request.POST:
            # Check if the delete button was clicked
            if not user.is_superuser:
                user.delete()
            return redirect('login')
        
        else:
            form = RenamePetForm(request.POST)
            if form.is_valid():
                new_pet_name = form.cleaned_data['pet_name']
                profile.pet_name = new_pet_name
                profile.save()
                # Redirect to prevent form resubmission on page refresh
                return redirect('profile')
    else:
        form = RenamePetForm()

    return render(request, "trashpetapp/profile.html", {"form": form, "username": username, "leaves": leaves, "pet_name": pet_name})


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

# login page - need a popup when user/password is incorrect
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
    return redirect('index')