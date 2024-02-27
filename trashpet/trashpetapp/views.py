from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm, RenamePetForm, CodeForm
from .models import UserProfile, Accessory
from django.contrib.auth.decorators import login_required

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
    cap = Accessory.objects.create(name="cap",type="normal", locked=False, price=0, link="images/cap.png")
    cap.save()
    socks = Accessory.objects.create(name="socks",type="normal", locked=False, price=0, link="images/socks.png")
    socks.save()
    crown = Accessory.objects.create(name="crown",type="normal", locked=False, price=0, link="images/crown.png")
    crown.save()
    bottle = Accessory.objects.create(name="bottle",type="normal", locked=False, price=0, link="images/bottle.png")
    bottle.save()

    cap_image = cap.link
    socks_image = socks.link
    crown_image = crown.link
    bottle_image = bottle.link

    cap_locked = cap.locked
    socks_locked = socks.locked
    crown_locked = crown.locked
    bottle_locked = bottle.locked

    return render(request, "trashpetapp/shop.html", {"cap_image": cap_image, "socks_image": socks_image, "crown_image":crown_image, "bottle_image":bottle_image, "cap_locked":cap_locked, "socks_locked":socks_locked, "crown_locked":crown_locked, "bottle_locked":bottle_locked})

@login_required
def map(request):
    return render(request, "trashpetapp/map.html")

@login_required
def garden(request):
    return render(request, "trashpetapp/garden.html")

@login_required
def camera(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)

    if request.method == 'POST':
        form = CodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            profile.codes = code
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