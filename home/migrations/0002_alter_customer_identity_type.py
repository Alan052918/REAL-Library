# Generated by Django 3.2.16 on 2022-12-11 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='identity_type',
            field=models.CharField(choices=[(0, 'Passport'), (1, 'SSN'), (2, "Driver's License")], max_length=20),
        ),
    ]
