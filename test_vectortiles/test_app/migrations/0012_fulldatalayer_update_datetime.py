# Generated by Django 3.2.17 on 2023-02-15 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test_app", "0011_fulldatalayer_include_in_tilejson"),
    ]

    operations = [
        migrations.AddField(
            model_name="fulldatalayer",
            name="update_datetime",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
