from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pid>", views.index, name="index_params"),
    path("write/", views.write, name="write"),
    path("process/", views.process, name="process"),
]
