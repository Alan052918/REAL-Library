from django.core.validators import MinLengthValidator
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=50)

    topic = models.ForeignKey(Topic, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("book", "author"),)

    def __str__(self) -> str:
        return f"{self.book} - {self.author}"


class Copy(models.Model):
    status = models.CharField(max_length=1, validators=[MinLengthValidator])

    book = models.ForeignKey(Book, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return f"book {self.book}"


class Rental(models.Model):
    status = models.CharField(max_length=1)
    borrow_date = models.DateField("borrowed date")
    expected_return = models.DateField("expected return date")
    actual_return = models.DateField("actual return date")

    copy = models.ForeignKey(Copy, on_delete=models.RESTRICT, null=True)

    class Meta:
        indexes = [models.Index(fields=["id"])]

    def __str__(self) -> str:
        return f"{self.id}"


class Invoice(models.Model):
    date = models.DateField("invoice date")
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)

    class Meta:
        indexes = [models.Index(fields=["id"])]

    def __str__(self) -> str:
        return f"{self.id}"


class Payment(models.Model):
    date = models.DateField("payment date")
    method = models.CharField(max_length=2, validators=[MinLengthValidator])
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.id}"
