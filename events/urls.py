"""reallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("exhibitions/", views.exhibitions_view, name="exhibitions"),
    path(
        "exhibitions/<int:pk>/",
        views.exhibition_detail_view,
        name="exhibition-detail",
    ),
    path("seminars/", views.seminars_view, name="seminars"),
    path("seminars/<int:pk>/", views.seminar_detail_view, name="seminar-detail"),
    path("sponsors/", views.sponsors_view, name="sponsors"),
    path("sponsors/<int:pk>/", views.sponsor_detail_view, name="sponsor-detail"),
]
