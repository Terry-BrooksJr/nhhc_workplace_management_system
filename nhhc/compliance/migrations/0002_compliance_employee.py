# Generated by Django 3.2.20 on 2023-07-21 23:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("compliance", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="compliance",
            name="employee",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]