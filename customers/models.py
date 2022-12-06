from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=50)
    identity_type = models.CharField(max_length=1)
    identity_number = models.CharField(max_length=15)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
