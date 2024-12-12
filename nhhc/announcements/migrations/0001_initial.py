# Generated by Django 5.1.4 on 2024-12-12 17:21

import django_prometheus.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Announcements",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("message", models.TextField()),
                ("announcement_title", models.CharField(default="", max_length=10485760)),
                ("date_posted", models.DateTimeField(auto_now=True)),
                ("message_type", models.CharField(choices=[("C", "Safety"), ("T", "Training"), ("X", "Compliance"), ("G", "General")], default="G", max_length=10485760)),
                ("status", models.CharField(choices=[("A", "Active"), ("D", "Draft"), ("X", "Archived")], db_index=True, default="D", max_length=10485760)),
            ],
            options={
                "verbose_name": "Internal Announcement",
                "verbose_name_plural": "Internal Announcements",
                "db_table": "announcements",
                "ordering": ["-date_posted", "status", "message_type"],
            },
            bases=(models.Model, django_prometheus.models.ExportModelOperationsMixin("announcements")),
        ),
    ]
