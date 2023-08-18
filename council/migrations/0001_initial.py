# Generated by Django 4.2.4 on 2023-08-18 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CouncilPost",
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
                ("council", models.CharField(max_length=128)),
                ("title", models.CharField(max_length=128)),
                ("category", models.CharField(max_length=128)),
                ("location", models.CharField(default="가천대학교", max_length=128)),
                ("remaining_cnt", models.IntegerField(default=0)),
                (
                    "council_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="council_posts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]