# Generated by Django 4.1 on 2022-08-27 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PostDump",
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
                ("content", models.TextField()),
                ("date_created", models.DateTimeField()),
            ],
        ),
    ]
