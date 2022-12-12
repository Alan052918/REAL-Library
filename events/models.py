from django.db import models

from inventory.models import Author, Topic


class Event(models.Model):
    EVENT_TYPE = [("Seminar", "Seminar"), ("Exhibition", "Exhibition")]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=10, choices=EVENT_TYPE)
    start_datetime = models.DateTimeField("start datetime")
    stop_datetime = models.DateTimeField("stop datetime")

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "{} {} {} {} {} topic: {} {}".format(
            self.id,
            self.name,
            self.type,
            self.start_datetime,
            self.stop_datetime,
            self.topic.id,
            self.topic.name,
        )


class Exhibition(Event):
    expense = models.FloatField(max_length=10)


class Sponsor(models.Model):
    SPONSOR_TYPE = [("Individual", "Individual"), ("Organization", "Organization")]

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    type = models.CharField(max_length=15, choices=SPONSOR_TYPE)

    def __str__(self):
        return f"{self.id} {self.first_name} {self.last_name} type: {self.type}"


class Seminar(Event):
    sponsors = models.ManyToManyField(Sponsor, through="SeminarSponsor")
    authors = models.ManyToManyField(Author, through="SeminarAuthor")


class SeminarSponsor(models.Model):
    seminar = models.ForeignKey(Seminar, on_delete=models.CASCADE)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = (("seminar", "sponsor"),)


class SeminarAuthor(models.Model):
    seminar = models.ForeignKey(Seminar, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("seminar", "author"),)
