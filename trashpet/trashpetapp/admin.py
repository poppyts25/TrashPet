from django.contrib import admin
from .models import UserProfile, Accessory
from .models import Marker
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Accessory)
admin.site.register(Marker)


# @admin.register(Marker)
# class MarkerAdmin(admin.ModelAdmin):
#     list_display = ("name", "location")