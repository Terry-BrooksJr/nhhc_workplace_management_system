# Generated by Django 5.0.6 on 2024-06-01 20:31

from django.db import migrations, models

import nhhc.utils.upload


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employmentapplicationmodel",
            name="cpr_card",
            field=models.FileField(blank=True, null=True, upload_to=nhhc.utils.upload.UploadHandler.generate_randomized_file_name),
        ),
        migrations.AlterField(
            model_name="employmentapplicationmodel",
            name="resume_cv",
            field=models.FileField(blank=True, null=True, upload_to=nhhc.utils.upload.UploadHandler.generate_randomized_file_name),
        ),
    ]
