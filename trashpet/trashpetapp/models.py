from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    leaves = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    pet_name = models.CharField(max_length=30, default="Trash Pet") # set different / validate pet name length???
    codes = models.CharField(max_length=30,default="")

    def __str__(self):
        return f"{self.user.username}"
    

class Accessory(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    locked = models.BooleanField()
    code = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    link = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
