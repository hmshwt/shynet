# Generated by Django 3.0.6 on 2020-05-07 20:28

from django.db import migrations, models

import core.models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_service_collect_ips"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="ignored_ips",
            field=models.TextField(
                blank=True, default="", validators=[core.models._validate_network_list]
            ),
        ),
    ]
