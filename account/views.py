from django.contrib import auth, messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("Hello from account.")


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
        return redirect("home_page")


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
        return redirect("home_page")


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect("home_page")
