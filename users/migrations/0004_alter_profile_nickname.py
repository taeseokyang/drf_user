# Generated by Django 4.2.4 on 2023-08-18 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_rename_borrow_cnd_profile_borrow_cnt"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="nickname",
            field=models.CharField(default="noNickname", max_length=128),
        ),
    ]