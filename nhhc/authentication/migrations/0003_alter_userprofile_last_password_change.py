# Generated by Django 5.0.4 on 2024-04-30 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="last_password_change",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]