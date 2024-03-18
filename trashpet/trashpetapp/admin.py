from django.contrib import admin
from .models import UserProfile, Accessory, Marker, LeavesCode
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Accessory)
admin.site.register(Marker)
admin.site.register(LeavesCode)


# @admin.register(Marker)
# class MarkerAdmin(admin.ModelAdmin):
#     list_display = ("name", "location")