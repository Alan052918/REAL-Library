# Generated by Django 3.2.16 on 2022-12-11 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_alter_rental_actual_return'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='copy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='inventory.copy'),
        ),
    ]