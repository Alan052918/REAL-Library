# Generated by Django 4.1.3 on 2022-12-07 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("phone", models.CharField(max_length=13)),
                ("email", models.EmailField(max_length=50)),
                ("identity_type", models.CharField(max_length=1)),
                ("identity_number", models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name="Room",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("capacity", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="RoomCustomer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("reserved_date", models.DateField(verbose_name="reserved date")),
                ("time_slot", models.IntegerField()),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="rooms.customer"
                    ),
                ),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="rooms.room"
                    ),
                ),
            ],
            options={
                "unique_together": {("room", "customer")},
            },
        ),
    ]