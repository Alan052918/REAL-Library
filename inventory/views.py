from django.http import HttpResponse
from django.shortcuts import render

from .models import Topic, Book, Author, BookAuthor, Copy, Rental, Invoice, Payment


def index(request):
    topic_list = Topic.objects.all()
    book_list = Book.objects.all()
    author_list = Author.objects.all()
    return render(
        request,
        "inventory/index.html",
        {"topic_list": topic_list, "book_list": book_list, "author_list": author_list},
    )


def topics_view(request):
    topic_list = Topic.objects.all()
    return render(request, "inventory/topics.html", {"topic_list": topic_list})


def topic_detail_view(request, pk):
    topic = Topic.objects.get(pk=pk)
    book_list = Book.objects.filter(topic__id=topic.id)
    return render(
        request, "inventory/topic_detail.html", {"topic": topic, "book_list": book_list}
    )


def books_view(request):
    book_list = Book.objects.all()
    return render(request, "inventory/books.html", {"book_list": book_list})


def book_detail_view(request, pk):
    book = Book.objects.get(pk=pk)
    copy_list = Copy.objects.filter(book__id=book.id)
    rental_list = Rental.objects.filter(copy__in=copy_list)

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


def authors_view(request):
    author_list = Author.objects.all()
    return render(request, "inventory/authors.html", {"author_list": author_list})


def author_detail_view(request, pk):
    author = Author.objects.get(pk=pk)

    book_authors = BookAuthor.objects.filter(author__id=author.id)
    if book_authors.exists():
        book_ids = book_authors.values_list("book", flat=True)
        book_list = Book.objects.filter(id__in=book_ids)

    return render(
        request,
        "inventory/author_detail.html",
        {"author": author, "book_list": book_list},
    )
