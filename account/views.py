from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Customer


@login_required(login_url="login")
def index(request):
    if request.method == "GET":
        login_user = request.user
        customer = Customer.objects.get(user=login_user)
        if not customer.exists():
            return redirect("signup")
        return render(request, "index.html", {"customer": customer})


def signup(request):
    if request.method == "GET":
        return render(request, "signup.html")

    if request.method == "POST":
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if len(User.objects.filter(username=username)) > 0:
            return render(request, "signup.html", {"check1": "Username already exists"})
        if password1 != password2:
            return render(request, "signup.html", {"check2": "Passwords do not match"})

        user = User.objects.create_user(username, make_password(password1))
        user.save()

        messages.success(request, f"Success! Welcome {username}")
        return redirect("signup_success")


def signup_success(request):
    return render(request, "signup_success.html")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if not user:
            return render(
                request, "login.html", {"check": "Username or password incorrect"}
            )
        auth.login(request, user)
        return redirect("index")


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect("home_page")
