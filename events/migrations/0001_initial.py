# Generated by Django 3.2.16 on 2022-12-10 00:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seminar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=10)),
                ('start_datetime', models.DateTimeField(verbose_name='start datetime')),
                ('stop_datetime', models.DateTimeField(verbose_name='stop datetime')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('type', models.CharField(max_length=1, validators=[django.core.validators.MinLengthValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='SeminarSponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('seminar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.seminar')),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.sponsor')),
            ],
        ),
        migrations.CreateModel(
            name='SeminarAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.author')),
                ('seminar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.seminar')),
            ],
        ),
        migrations.AddField(
            model_name='seminar',
            name='authors',
            field=models.ManyToManyField(through='events.SeminarAuthor', to='inventory.Author'),
        ),
        migrations.AddField(
            model_name='seminar',
            name='sponsors',
            field=models.ManyToManyField(through='events.SeminarSponsor', to='events.Sponsor'),
        ),
        migrations.AddField(
            model_name='seminar',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.topic'),
        ),
        migrations.CreateModel(
            name='Exhibition',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=10)),
                ('start_datetime', models.DateTimeField(verbose_name='start datetime')),
                ('stop_datetime', models.DateTimeField(verbose_name='stop datetime')),
                ('expense', models.FloatField(max_length=10)),
                ('topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.topic')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
