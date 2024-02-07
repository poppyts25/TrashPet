from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    #template = loader.get_template("trashpetapp/home.html")
    return render(request, "trashpetapp/home.html")

def login(request):
    return render(request, "trashpetapp/login.html")

def shop(request):
    return HttpResponse("Shop")

def map(request):
    return HttpResponse("map")

def camera(request):
    return HttpResponse("camera")