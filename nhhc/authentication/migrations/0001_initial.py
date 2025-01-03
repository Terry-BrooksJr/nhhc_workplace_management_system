# Generated by Django 5.1.4 on 2025-01-03 08:41

import django_extensions.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created", django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name="created")),
                ("modified", django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name="modified")),
                ("force_password_change", models.BooleanField(default=True)),
                ("last_password_change", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "get_latest_by": "modified",
                "abstract": False,
            },
        ),
    ]
