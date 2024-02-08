from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Member(models.Model): # AbstractUser): 
    username = models.CharField(max_length = 255)
    petname = models.CharField(max_length = 255)
    petals = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.username}"
    

