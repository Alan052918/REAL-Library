from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=50)
    identity_type = models.CharField(max_length=1)
    identity_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Room(models.Model):
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.id}"


class RoomCustomer(models.Model):
    reserved_date = models.DateField("reserved date")
    time_slot = models.IntegerField()

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("room", "customer"),)

    def __str__(self):
        return f"room: {self.room} customer: {self.customer}"
