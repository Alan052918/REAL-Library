from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Exhibition, Seminar, Sponsor, SeminarAuthor, SeminarSponsor
from inventory.models import Author


def index(request):
    exhibition_list = Exhibition.objects.all()
    seminar_list = Seminar.objects.all()
    individual_sponsor_list = Sponsor.objects.filter(type="Individual")
    organization_sponsor_list = Sponsor.objects.filter(type="Organization")
    return render(
        request,
        "events/index.html",
        {
            "exhibition_list": exhibition_list,
            "seminar_list": seminar_list,
            "individual_sponsor_list": individual_sponsor_list,
            "organization_sponsor_list": organization_sponsor_list,
            "active_tab": "exhibitions",
        },
    )


@login_required(login_url="/login/")
def exhibition_detail_view(request, pk):
    exhibition = Exhibition.objects.get(pk=pk)
    return render(request, "events/exhibition_detail.html", {"exhibition": exhibition})


def seminars_tab(request):
    exhibition_list = Exhibition.objects.all()
    seminar_list = Seminar.objects.all()
    individual_sponsor_list = Sponsor.objects.filter(type="Individual")
    organization_sponsor_list = Sponsor.objects.filter(type="Organization")
    return render(
        request,
        "events/index.html",
        {
            "exhibition_list": exhibition_list,
            "seminar_list": seminar_list,
            "individual_sponsor_list": individual_sponsor_list,
            "organization_sponsor_list": organization_sponsor_list,
            "active_tab": "seminars",
        },
    )


@login_required(login_url="/login/")
def seminar_detail_view(request, pk):
    seminar = Seminar.objects.get(pk=pk)

    sponsor_list = []
    seminar_sponsors = SeminarSponsor.objects.filter(seminar__id=seminar.id)
    if seminar_sponsors.exists():
        sponsor_ids = seminar_sponsors.values_list("sponsor", flat=True)
        sponsors = Sponsor.objects.filter(id__in=sponsor_ids)
        sponsor_amounts = seminar_sponsors.values_list("amount", flat=True)
        sponsor_list = list(zip(sponsors, sponsor_amounts))

    author_list = []
    seminar_authors = SeminarAuthor.objects.filter(seminar__id=seminar.id)
    if seminar_authors.exists():
        author_ids = seminar_authors.values_list("author", flat=True)
        author_list = Author.objects.filter(id__in=author_ids)

    return render(
        request,
        "events/seminar_detail.html",
        {"seminar": seminar, "sponsor_list": sponsor_list, "author_list": author_list},
    )


def sponsors_tab(request):
    exhibition_list = Exhibition.objects.all()
    seminar_list = Seminar.objects.all()
    individual_sponsor_list = Sponsor.objects.filter(type="Individual")
    organization_sponsor_list = Sponsor.objects.filter(type="Organization")
    return render(
        request,
        "events/index.html",
        {
            "exhibition_list": exhibition_list,
            "seminar_list": seminar_list,
            "individual_sponsor_list": individual_sponsor_list,
            "organization_sponsor_list": organization_sponsor_list,
            "active_tab": "sponsors",
        },
    )


@login_required(login_url="/login/")
def sponsor_detail_view(request, pk):
    sponsor = Sponsor.objects.get(pk=pk)

    seminar_list = []
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
