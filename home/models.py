from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    IDENTITY_TYPE = [(0, "Passport"), (1, "SSN"), (2, "Driver's License")]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13)
    identity_type = models.CharField(max_length=20, choices=IDENTITY_TYPE)
    identity_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
