from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
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
    user_form = UserCreationForm()
    customer_form = CustomerCreationForm()

    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        customer_form = CustomerCreationForm(request.POST)
        if not user_form.is_valid() or not customer_form.is_valid():
            messages.error(request, "Invalid form!")
            for errors in user_form.errors.values():
                for error in errors:
                    messages.error(request, error)
            for errors in customer_form.errors.values():
                for error in errors:
                    messages.error(request, error)
        else:
            user = user_form.save()
            group = Group.objects.get(name="customer")
            if not group:
                messages.error(request, "Group not found!")
            else:
                user.groups.add(group)
                customer = customer_form.save(commit=False)
                customer.user = user
                customer.save()
                messages.success(request, "Account created successfully!")
                return redirect("/login/")

    return render(
        request,
        "home/signup.html",
        {"user_form": user_form, "customer_form": customer_form},
    )


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
