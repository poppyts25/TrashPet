from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("map/", views.map, name="map"),
    path("shop/", views.shop, name="shop"),
    path("camera/", views.camera, name="camera"),
    path("login/", views.login, name="login"),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
]