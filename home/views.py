from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render

from .decorators import unauthenticated_user
from .forms import CustomerCreationForm


def index(request):
    return render(request, "home/index.html")


@login_required(login_url="/login/")
def account(request):
    return render(request, "home/account.html", {"user": request.user})


def signup(request):
    form = CustomerCreationForm()

    if request.method == "POST":
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name="customer")
            user.groups.add(group)
            messages.success(request, "Account created successfully!")
            return redirect("/login/")

    return render(request, "home/signup.html", {"form": form})


@unauthenticated_user
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")

        messages.info(request, "Invalid credentials!")

    return render(request, "home/login.html")


@login_required(login_url="/login/")
def logout(request):
    auth.logout(request)
    return redirect("/")


def unauthorized(request):
    return render(request, "home/unauthorized.html")
