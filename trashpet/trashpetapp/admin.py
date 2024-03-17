from django.contrib import admin
from .models import UserProfile, Accessory, LeavesCode

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Accessory)
admin.site.register(LeavesCode)