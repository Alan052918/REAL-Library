from django.db import models

from home.models import Customer


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    capacity = models.IntegerField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} capacity: {self.capacity} location: {self.location}"


class RoomCustomer(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    reserved_date = models.DateField("reserved date")
    time_slot = models.IntegerField()

    class Meta:
        unique_together = (("room", "customer"),)

    def __str__(self):
        return f"room: {self.room} customer: {self.customer}"
