from django.urls import path, include
from django.contrib import admin

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("walking/", views.map, name="map"),
    path("shop/", views.shop, name="shop"),
    path("buy_accessory/", views.buy_accessory, name="buy_accessory"),
    path("save_accessories/", views.save_accessories, name="save_accessories"),
    path("codes/", views.codes, name="codes"),
    path("admin/", admin.site.urls),
    path("login/", views.user_login, name='login'),
    path("signup/", views.user_signup, name='signup'),
    path("logout/", views.user_logout, name='logout'),
    path("profile/", views.profile, name='profile'),
    path("garden/", views.garden, name="garden"),
    path('update_map_leaves/', views.update_map_leaves, name='update_map_leaves'),
    path('update_leaves/', views.update_leaves, name='update_leaves'),
    path("policy/", views.policy, name="policy"),
    path("gamemaker/", views.gamemaker, name="gamemaker"),
    path("gamemakercreation/", views.gamemakercreation, name="gamemakercreation")
]
