from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path("login/", views.try_login, name="login"),
    path("logout/", views.try_logout, name="logout"),
    path("create/", views.create, name="create"),
]
