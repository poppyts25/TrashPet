from django.contrib.auth.models import User,Permission
from django.db import models
from django.contrib.gis.db import models



import json


# User Profile: Leaves are currency, locked_list designates unlocked accessories
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    leaves = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    pet_name = models.CharField(max_length=30, default="Trash Pet") # set different / validate pet name length???
    locked_list = {"Cap":False, "Crown":False, "Socks":False, "Bottle":True }
    locked_list = json.dumps(locked_list)               
    accessories = models.CharField(max_length=200, default=locked_list)

    bought_list = {"Cap":False, "Crown":False, "Socks":False, "Bottle":False }
    bought_list = json.dumps(bought_list) 
    bought = models.CharField(max_length=200, default=bought_list)




    def __str__(self):
        return f"{self.user.username}"
    

# Accessory: stores information about each store item
class Accessory(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    locked = models.BooleanField()
    code = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    link = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class LeavesCode(models.Model):
    name = models.CharField(max_length=20)
    leaves = models.DecimalField(max_digits=5, decimal_places = 0)

    def __str__(self):
        return f"{self.name}"

class CustomUserPermissions:
    class Meta:
        permissions = (
            ("gamemaker", "Can add event unlocks")
        )
    
class Marker(models.Model):
    name = models.CharField(
        max_length=255
    )
    location = models.PointField()

    def __str__(self):
        return self.name

