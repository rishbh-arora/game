from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("stats", views.stats),
    path("login", views.login)
]
