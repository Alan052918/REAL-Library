from django.contrib import auth, messages
from django.shortcuts import redirect, render

from .forms import CustomerCreationForm


def index(request):
    return render(request, "home/index.html")


def signup(request):
    if request.user.is_authenticated:
        return redirect("/")

    form = CustomerCreationForm()

    if request.method == "POST":
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect("/login/")

    return render(request, "home/signup.html", {"form": form})


def login(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")

        messages.info(request, "Invalid credentials!")

    return render(request, "home/login.html")


def logout(request):
    auth.logout(request)
    return redirect("/")
