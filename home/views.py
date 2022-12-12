from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render

from .decorators import unauthenticated_user
from .forms import CustomerCreationForm

from events.models import Exhibition, ExhibitionUser
from inventory.models import Rental, Invoice, Payment


def index(request):
    return render(request, "home/index.html")


@login_required(login_url="/login/")
def account(request):
    borrowed_list = Rental.objects.filter(user__id=request.user.id, status="Borrowed")
    returned_list = Rental.objects.filter(user__id=request.user.id, status="Returned")
    overdue_list = Rental.objects.filter(user__id=request.user.id, status="Overdue")

    invoice_list = Invoice.objects.filter(
        rental__id__in=returned_list.values_list("id", flat=True)
    )

    exhibition_list = []
    exhibition_users = ExhibitionUser.objects.filter(user__id=request.user.id)
    if exhibition_users.exists():
        exhibition_ids = exhibition_users.values_list("exhibition", flat=True)
        exhibition_list = Exhibition.objects.filter(id__in=exhibition_ids)

    return render(
        request,
        "home/account.html",
        {
            "user": request.user,
            "borrowed_list": borrowed_list,
            "returned_list": returned_list,
            "overdue_list": overdue_list,
            "invoice_list": invoice_list,
            "exhibition_list": exhibition_list,
            "active_tab": "profile",
        },
    )


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

        messages.error(request, "Invalid credentials!")

    return render(request, "home/login.html")


@login_required(login_url="/login/")
def logout(request):
    auth.logout(request)
    return redirect("/")


def unauthorized(request):
    return render(request, "home/unauthorized.html")
