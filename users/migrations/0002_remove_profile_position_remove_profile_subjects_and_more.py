# Generated by Django 4.2.4 on 2023-08-18 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="profile", name="position",),
        migrations.RemoveField(model_name="profile", name="subjects",),
        migrations.AddField(
            model_name="profile",
            name="borrow_cnd",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="profile", name="lend_cnt", field=models.IntegerField(default=0),
        ),
    ]
