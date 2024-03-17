from django.urls import path, include
from django.contrib import admin

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("map/", views.map, name="map"),
    path("shop/", views.shop, name="shop"),
    path("codes/", views.codes, name="codes"),
    path("admin/", admin.site.urls),
    path("login/", views.user_login, name='login'),
    path("signup/", views.user_signup, name='signup'),
    path("logout/", views.user_logout, name='logout'),
    path("profile/", views.profile, name='profile'),
    path("garden/", views.garden, name="garden"),
    path('update_leaves/', views.update_leaves, name='update_leaves'),
    path('total-distance/', views.calculate_total_distance, name='calculate_total_distance'),
    path('track-journey/', views.track_journey, name='track_journey'),
    
    
]