from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Customer


@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)


@receiver(post_save, sender=User)
def update_customer(sender, instance, created, **kwargs):
    if not created:
        instance.customer.save()