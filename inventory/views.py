from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Topic, Book, Author, BookAuthor, Copy, Rental, Invoice, Payment


def index(request):
    topic_list = Topic.objects.all()
    book_list = Book.objects.all()
    author_list = Author.objects.all()
    return render(
        request,
        "inventory/index.html",
        {
            "topic_list": topic_list,
            "book_list": book_list,
            "author_list": author_list,
            "active_tab": "topics",
        },
    )


@login_required(login_url="/login/")
def topic_detail_view(request, pk):
    topic = Topic.objects.get(pk=pk)
    book_list = Book.objects.filter(topic__id=topic.id)
    return render(
        request, "inventory/topic_detail.html", {"topic": topic, "book_list": book_list}
    )


def books_tab(request):
    topic_list = Topic.objects.all()
    book_list = Book.objects.all()
    author_list = Author.objects.all()
    return render(
        request,
        "inventory/index.html",
        {
            "topic_list": topic_list,
            "book_list": book_list,
            "author_list": author_list,
            "active_tab": "books",
        },
    )


@login_required(login_url="/login/")
def book_detail_view(request, pk):
    book = Book.objects.get(pk=pk)
    copy_list = Copy.objects.filter(book__id=book.id)
    rental_list = Rental.objects.filter(copy__in=copy_list)

    author_list = []
    book_authors = BookAuthor.objects.filter(book__id=book.id)
    if book_authors.exists():
        author_ids = book_authors.values_list("author", flat=True)
        author_list = Author.objects.filter(id__in=author_ids)

    return render(
        request,
        "inventory/book_detail.html",
        {
            "book": book,
            "copy_list": copy_list,
            "rental_list": rental_list,
            "author_list": author_list,
        },
    )


@login_required(login_url="/login/")
def copy_detail_view(request, pk, copy_pk):
    book = Book.objects.get(pk=pk)
    copy = Copy.objects.get(pk=copy_pk)
    rental_list = Rental.objects.filter(copy__id=copy.id)
    return render(
        request,
        "inventory/copy_detail.html",
        {"book": book, "copy": copy, "rental_list": rental_list},
    )


def authors_tab(request):
    topic_list = Topic.objects.all()
    book_list = Book.objects.all()
    author_list = Author.objects.all()
    return render(
        request,
        "inventory/index.html",
        {
            "topic_list": topic_list,
            "book_list": book_list,
            "author_list": author_list,
            "active_tab": "authors",
        },
    )


def author_detail_view(request, pk):
    author = Author.objects.get(pk=pk)

    book_list = []
    book_authors = BookAuthor.objects.filter(author__id=author.id)
    if book_authors.exists():
        book_ids = book_authors.values_list("book", flat=True)
        book_list = Book.objects.filter(id__in=book_ids)

    return render(
        request,
        "inventory/author_detail.html",
        {"author": author, "book_list": book_list},
    )
