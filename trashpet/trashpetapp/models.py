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
    

