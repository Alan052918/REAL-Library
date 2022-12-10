from django.shortcuts import render

from .models import Exhibition, Seminar, Sponsor, SeminarAuthor, SeminarSponsor
from inventory.models import Author


def index(request):
    exhibition_list = Exhibition.objects.all()
    seminar_list = Seminar.objects.all()
    sponsor_list = Sponsor.objects.all()
    return render(
        request,
        "events/index.html",
        {
            "exhibition_list": exhibition_list,
            "seminar_list": seminar_list,
            "sponsor_list": sponsor_list,
        },
    )


def exhibition_detail_view(request, pk):
    exhibition = Exhibition.objects.get(pk=pk)
    return render(request, "events/exhibition_detail.html", {"exhibition": exhibition})


def seminar_detail_view(request, pk):
    seminar = Seminar.objects.get(pk=pk)

    seminar_sponsors = SeminarSponsor.objects.filter(seminar__id=seminar.id)
    if seminar_sponsors.exists():
        sponsor_ids = seminar_sponsors.values_list("sponsor", flat=True)
        sponsors = Sponsor.objects.filter(id__in=sponsor_ids)
        sponsor_amounts = seminar_sponsors.values_list("amount", flat=True)
        sponsor_list = list(zip(sponsors, sponsor_amounts))

    seminar_authors = SeminarAuthor.objects.filter(seminar__id=seminar.id)
    if seminar_authors.exists():
        author_ids = seminar_authors.values_list("author", flat=True)
        author_list = Author.objects.filter(id__in=author_ids)

    return render(
        request,
        "events/seminar_detail.html",
        {"seminar": seminar, "sponsor_list": sponsor_list, "author_list": author_list},
    )


def sponsor_detail_view(request, pk):
    sponsor = Sponsor.objects.get(pk=pk)

    seminar_sponsors = SeminarSponsor.objects.filter(sponsor__id=sponsor.id)
    if seminar_sponsors.exists():
        seminar_ids = seminar_sponsors.values_list("seminar", flat=True)
        seminars = Seminar.objects.filter(id__in=seminar_ids)
        sponsor_amounts = seminar_sponsors.values_list("amount", flat=True)
        seminar_list = list(zip(seminars, sponsor_amounts))

    return render(
        request,
        "events/sponsor_detail.html",
        {"sponsor": sponsor, "seminar_list": seminar_list},
    )
