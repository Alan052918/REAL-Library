from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.signup, name="login"),
    path("logout/", views.signup, name="logout"),
]
