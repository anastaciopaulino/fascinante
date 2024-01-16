# Generated by Django 5.0.1 on 2024-01-16 12:53

import django.db.models.deletion
import schedules.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("services", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Scheduling",
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
                ("author", models.CharField(max_length=200)),
                (
                    "checkin",
                    models.CharField(
                        max_length=20,
                        validators=[
                            schedules.models.validate_data_hora,
                            schedules.models.validate_horario,
                        ],
                    ),
                ),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="services.service",
                    ),
                ),
            ],
        ),
    ]