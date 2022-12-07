# Generated by Django 4.1.3 on 2022-12-07 02:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("inventory", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=30)),
                ("type", models.CharField(max_length=10)),
                ("start_datetime", models.DateTimeField(verbose_name="start datetime")),
                ("stop_datetime", models.DateTimeField(verbose_name="stop datetime")),
                (
                    "topic",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.topic",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Sponsor",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30, null=True)),
                (
                    "type",
                    models.CharField(
                        max_length=1,
                        validators=[django.core.validators.MinLengthValidator(1)],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Exhibition",
            fields=[
                (
                    "event_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="events.event",
                    ),
                ),
                ("expense", models.FloatField(max_length=10)),
            ],
            bases=("events.event",),
        ),
        migrations.CreateModel(
            name="Seminar",
            fields=[
                (
                    "event_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="events.event",
                    ),
                ),
            ],
            bases=("events.event",),
        ),
        migrations.CreateModel(
            name="SeminarSponsor",
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
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "sponsor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="events.sponsor"
                    ),
                ),
                (
                    "seminar",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="events.seminar"
                    ),
                ),
            ],
            options={
                "unique_together": {("seminar", "sponsor")},
            },
        ),
        migrations.CreateModel(
            name="SeminarAuthor",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.author",
                    ),
                ),
                (
                    "seminar",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="events.seminar"
                    ),
                ),
            ],
            options={
                "unique_together": {("seminar", "author")},
            },
        ),
    ]