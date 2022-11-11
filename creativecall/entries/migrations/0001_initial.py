# Generated by Django 3.2.13 on 2022-04-18 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Choice",
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
                ("choice_text", models.CharField(max_length=200)),
                ("votes", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Criteria",
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
                ("criteria_name", models.CharField(max_length=30)),
                ("parent_id", models.IntegerField(default=0)),
            ],
        ),
    ]
