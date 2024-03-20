from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm, RenamePetForm, CodeForm, GamemakerForm, LeavesCodeForm
from .models import UserProfile, Accessory, LeavesCode,Marker
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
import json
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType




def map(request):
    markers = Marker.objects.all()
    user = request.user
    profile = UserProfile.objects.get(user=user)
    leaves = profile.leaves
    return render(request, 'trashpetapp/map.html', {"leaves":leaves,"markers":markers})

def index(request): 
    return render(request, "trashpetapp/index.html")

def is_gamemaker(user):
    return user.groups.filter(name='Gamemaker').exists()

@login_required
@user_passes_test(is_gamemaker)
def gamemaker(request): 

    if request.method == 'POST':
        if 'gamemaker_form' in request.POST:
            form = GamemakerForm(request.POST)
            
            if form.is_valid():

                item_name = form.cleaned_data['item_name']
                item_type = form.cleaned_data['item_type']
                item_code = form.cleaned_data['item_code']
                item_price = form.cleaned_data['item_price']
                item_link = form.cleaned_data['item_link']
                item = Accessory.objects.create(name=item_name, type=item_type, locked= True, code=item_code, price=item_price, link=item_link)
                item.save()

                for user in UserProfile.objects.all():

                    locked_list = user.locked_list
                    bought_list = user.bought_list
                    accessories = user.accessories

                    try:
                        locked_list = json.loads(locked_list)
                    except:
                        locked_list = {"":""}

                    try:
                        bought_list = json.loads(bought_list)
                    except:
                        bought_list = {"":""}
                    
                    try:
                        accessories = json.loads(accessories)
                    except:
                        accessories = {"":""}
                    
                    locked_list[item_name] = True
                    bought_list[item_name] = True
                    accessories[item_name] = False

                    user.locked_list = locked_list
                    user.bought_list = bought_list
                    user.accessories = accessories

                    user.save()

                return redirect("shop")
        else:
            form = GamemakerForm()
        if 'leavescode_form' in request.POST:  
            form2 = LeavesCodeForm(request.POST)
            if form2.is_valid():
                code = form2.cleaned_data['code']
                leaves = form2.cleaned_data['leaves']
                LeavesCode.objects.create(name=code, leaves=leaves)
            return redirect("shop")
        
        else:
            form2 = LeavesCodeForm()

    else:
        form = GamemakerForm()
        form2 = LeavesCodeForm()

    return render(request, "trashpetapp/gamemaker.html", {"form": form, "form2": form2})


@login_required # Automatically redirects to login page if not logged in
def home(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    petname = profile.pet_name
    #list of item links
    accessories = Accessory.objects.all()
    user_accessories = profile.accessories

    try:
        user_accessories = json.loads(user_accessories)
    except:
        user_accessories = {"":""}

    items = []
    for accessory in accessories:
        if user_accessories[accessory.name]:
            items.append('/static/images/'+accessory.link)

    items = json.dumps(items)
    pet_colour = json.dumps(profile.pet_colour)
    
    return render(request, "trashpetapp/home.html", {"petname": petname, "accessories":items, "pet_colour": pet_colour})

@login_required
def shop(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    locked_list = profile.locked_list
    bought_list = profile.bought_list

    # Loads unlocked accessories
    try:
        locked_list = json.loads(locked_list)
    except:
        locked_list = {"":""}

    # Loads bought accessories
    try:
        bought_list = json.loads(bought_list)
    except:
        bought_list = {"":""}

    accessories = Accessory.objects.all()
    
    user_accessories = profile.accessories
    try:
        user_accessories = json.loads(user_accessories)
    except:
        user_accessories = {"":""}

    items = []
    for accessory in accessories:
        if user_accessories[accessory.name]:
            items.append('/static/images/'+accessory.link)

    items = json.dumps(items)
    pet_colour = json.dumps(profile.pet_colour)
    return render(request, "trashpetapp/shop.html", {"accessories": accessories, "pet_colour":pet_colour, "locked_list": locked_list, "bought_list": bought_list, "leaves": profile.leaves, "items":  items, "equipped_list": profile.accessories})


def save_accessories(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    user_accessories = profile.accessories

    try:
        user_accessories = json.loads(user_accessories)
    except:
        user_accessories = {"":""}
    
    if request.method == 'POST':
        user_accessories = {}
        new_accessory_list = request.POST.get('accessories')
        try:
            new_accessory_list = json.loads(new_accessory_list)
        except:
            new_accessory_list = []
        
        accessories = Accessory.objects.all()

        for accessory in accessories:
            if "/static/images/"+accessory.link in new_accessory_list:
                user_accessories[accessory.name] = True
            else:
                user_accessories[accessory.name] = False
   

        user_accessories = json.dumps(user_accessories)
        
        profile.pet_colour = request.POST.get('pet_colour')
        profile.accessories = user_accessories
        profile.save()

        return redirect("home")
    
    return JsonResponse({"message":"Accessories Saved Successfully"})


def buy_accessory(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    leaves = profile.leaves
    bought_list = profile.bought_list
    #loads bought accessories
    try:
        bought_list = json.loads(bought_list)
    except:
        bought_list = {"":""}

    if request.method == 'POST':
        # Get the new leaves value from the POST data
        new_leaves = request.POST.get('new_leaves')
        
        # Update the leaves value
        profile.leaves=new_leaves
        profile.save()

        # Checks accessories and if they match sets that accessory to "bought"
        accessories = Accessory.objects.all()
        accessory_name = request.POST.get('accessory_name')
        for accessory in accessories:
            if accessory.name == accessory_name:
                bought_list[accessory.name] = True
                bought_list = json.dumps(bought_list)
                profile.bought_list = bought_list
                profile.save()
                break
        
        return JsonResponse({'new_leaves': new_leaves, 'accessory_name': accessory_name})
    else:
        # Handle other HTTP methods if necessary
        return render(request, 'trashpetapp/shop.html', {'leaves': 0})
    

@login_required
def map(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    leaves = profile.leaves
    return render(request, "trashpetapp/map.html", {'leaves': leaves})

@login_required
def garden(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    leaves = profile.leaves
    accessories = Accessory.objects.all()
    user_accessories = profile.accessories
    try:
        user_accessories = json.loads(user_accessories)
    except:
        user_accessories = {"":""}

    items = []
    for accessory in accessories:
        if user_accessories[accessory.name]:
            items.append('/static/images/'+accessory.link)

    items = json.dumps(items)
    pet_colour = json.dumps(profile.pet_colour)

    data = {"leaves":leaves, "accessories": items, "pet_colour": pet_colour} #view that handles ajax request
    return render(request, "trashpetapp/garden.html", data)

def update_leaves(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    leaves = profile.leaves
    if request.method == 'POST':
        # Get the new leaves value from the POST data
        new_leaves = request.POST.get('new_leaves')
        
        # Update the leaves value
        profile.leaves=new_leaves
        profile.save()
        
        return JsonResponse({'new_leaves': new_leaves})
    else:
        # Handle other HTTP methods if necessary
        return render(request, 'trashpetapp/garden.html', {'leaves': 0})
def update_map_leaves(request):
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
        return render(request, 'trashpetapp/walking.html', {'leaves': 0})
    


@login_required
def codes(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    locked_list = profile.locked_list
    bought_list = profile.bought_list

    #loads unlocked accessories list
    try:
        locked_list = json.loads(locked_list)
    except:
        locked_list = {"":""}
    
    #loads bought accessories
    try:
        bought_list = json.loads(bought_list)
    except:
        bought_list = {"":""}
    
    accessories = Accessory.objects.all()
    leavescodes = LeavesCode.objects.all()
    found = False
    

    if request.method == 'POST':
        form = CodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            
            #checks accessory unlock codes, and if one is correct sets that accessory to "unlocked"
            for accessory in accessories:
                if accessory.code == code:
                    name = accessory.name
                    locked_list[name] = False
                    locked_list = json.dumps(locked_list)
                    profile.locked_list = locked_list
                    # Add to bought list
                    bought_list[name] = True
                    bought_list = json.dumps(bought_list)
                    profile.bought_list = bought_list
                    profile.save()
                    found = True
                    break
            
            if not found:
                for leavescode in leavescodes:
                    if leavescode.name == code:
                        prize = leavescode.leaves
                        profile.leaves += prize
                        profile.save()
                        break

            return redirect("shop")
    else:
        form = CodeForm()
    return render(request, "trashpetapp/codes.html", {"form": form})

@login_required 
def profile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    username = user.username
    leaves = profile.leaves
    pet_name = profile.pet_name

    if request.method == 'POST':
        # Check if the delete button was clicked
        if 'delete_user' in request.POST:
            # Only delete regular users
            if not user.is_superuser:
                user.delete()
                profile.delete()
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

    return render(request, "trashpetapp/profile.html", {"form": form, "username": username, "leaves": leaves, "pet_name": pet_name, "is_gamemaker": is_gamemaker(user)})



def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():

            # Create user
            user = form.save()
            profile = UserProfile.objects.create(user=user)
            accessories = Accessory.objects.all()
            locked_list = {}
            bought_list = {}
            user_accessories = {}

            # Set all items to unbought and locked items to locked
            for accessory in accessories:
                accessory_name = accessory.name
                locked_list[accessory_name] = accessory.locked
                user_accessories[accessory_name] = False
                if accessory.locked:
                    bought_list[accessory_name] = True
                else:
                    bought_list[accessory_name] = False

            profile.locked_list = json.dumps(locked_list) 
            profile.bought_list = json.dumps(bought_list) 
            profile.accessories = json.dumps(user_accessories)
            profile.save()

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
    return redirect('index')


#policy page
def policy(request): 
    return render(request, "trashpetapp/policy.html")


def is_admin(user):
   return user.is_superuser

@user_passes_test(is_admin)
def gamemakercreation(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():

            # Create user
            user = form.save()
           
            # Add to gamemaker group
            gamemaker, created = Group.objects.get_or_create(name='Gamemaker')
            user.groups.add(gamemaker)
            user.save()

            # Create their profile
            profile = UserProfile.objects.create(user=user)
            accessories = Accessory.objects.all()
            locked_list = {}
            bought_list = {}
            user_accessories = {}

            # Set all items to unbought and locked items to locked
            for accessory in accessories:
                accessory_name = accessory.name
                locked_list[accessory_name] = accessory.locked
                user_accessories[accessory_name] = False
                if accessory.locked:
                    bought_list[accessory_name] = True
                else:
                    bought_list[accessory_name] = False

            profile.locked_list = json.dumps(locked_list) 
            profile.bought_list = json.dumps(bought_list)
            profile.accessories = json.dumps(user_accessories)

            profile.save()

            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'trashpetapp/gamemakercreation.html', {'form': form})

