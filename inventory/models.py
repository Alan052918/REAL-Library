from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=50)

    topic = models.ForeignKey(Topic, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zipcode = models.CharField(max_length=5, validators=[MinLengthValidator(5)])

    books = models.ManyToManyField(Book, through="BookAuthor")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("book", "author"),)

    def __str__(self):
        return f"{self.book.name} - {self.author.first_name} {self.author.last_name}"


class Copy(models.Model):
    COPY_STATUS = [
        ("Available", "Available"),
        ("Borrowed", "Borrowed"),
        ("Lost", "Lost"),
        ("Damaged", "Damaged"),
    ]

    status = models.CharField(max_length=10, choices=COPY_STATUS)

    book = models.ForeignKey(Book, on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.id} {self.status} book: {self.book.id} {self.book.name}"


class Rental(models.Model):
    RENTAL_STATUS = [
        ("Borrowed", "Borrowed"),
        ("Returned", "Returned"),
        ("Overdue", "Overdue"),
    ]

    status = models.CharField(max_length=10, choices=RENTAL_STATUS)
    borrow_date = models.DateField("borrowed date")
    expected_return = models.DateField("expected return date")
    actual_return = models.DateField("actual return date", null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    copy = models.ForeignKey(Copy, on_delete=models.RESTRICT)

    class Meta:
        indexes = [models.Index(fields=["id"])]

    def __str__(self):
        return "{} {} {} copy: {}".format(
            self.id, self.status, self.borrow_date, self.copy.id
        )


class Invoice(models.Model):
    date = models.DateField("invoice date")
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)

    class Meta:
        indexes = [models.Index(fields=["id"])]

    def __str__(self):
        return f"{self.id} {self.date} {self.amount} rental: {self.rental.id}"


class Payment(models.Model):
    PAYMENT_METHOD = [
        ("Cash", "Cash"),
        ("Credit", "Credit"),
        ("Debit", "Debit"),
        ("PayPal", "PayPal"),
    ]

    date = models.DateField("payment date")
    method = models.CharField(max_length=10, choices=PAYMENT_METHOD)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} {} {} {} {} invoice: {}".format(
            self.id,
            self.date,
            self.first_name,
            self.last_name,
            self.method,
            self.amount,
            self.invoice.id,
        )
