# Generated by Django 5.1.4 on 2024-12-12 17:22

from django.db import migrations, models

import nhhc.utils.upload


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employmentapplicationmodel",
            name="resume_cv",
            field=models.FileField(blank=True, null=True, upload_to=nhhc.utils.upload.UploadHandler.generate_randomized_file_name),
        ),
    ]
