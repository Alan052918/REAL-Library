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
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("topics/", views.topics_view, name="topics"),
    path("topics/<int:pk>/", views.topic_detail_view, name="topic-detail"),
    path("books/", views.books_view, name="books"),
    path("books/<int:pk>/", views.book_detail_view, name="book-detail"),
    path(
        "books/<int:pk>/copies/<int:copy_pk>/",
        views.copy_detail_view,
        name="copy-detail",
    ),
    path("authors/", views.authors_view, name="authors"),
    path("authors/<int:pk>/", views.author_detail_view, name="author-detail"),
]
