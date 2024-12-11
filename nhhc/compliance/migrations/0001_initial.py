# Generated by Django 5.1.1 on 2024-10-01 22:08

import django.db.models.deletion
import django_extensions.db.fields
import django_prometheus.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("employee", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contract",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created", django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name="created")),
                ("modified", django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name="modified")),
                ("code", models.CharField(max_length=10, unique=True)),
                ("name", models.CharField(max_length=10485760)),
                ("description", models.TextField(blank=True, null=True)),
                ("contract_year_start", models.DateField(blank=True, null=True, verbose_name="Start Year")),
                ("contract_year_end", models.DateField(blank=True, null=True, verbose_name="End Year")),
                ("active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "State Contract",
                "verbose_name_plural": "State Contracts",
                "db_table": "contracts",
                "ordering": ["-contract_year_start"],
            },
            bases=(models.Model, django_prometheus.models.ExportModelOperationsMixin("contracts")),
        ),
        migrations.CreateModel(
            name="Compliance",
            fields=[
                ("created", django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name="created")),
                ("modified", django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name="modified")),
                ("employee", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name="compliance_profile_of", serialize=False, to=settings.AUTH_USER_MODEL)),
                ("aps_check_passed", models.BooleanField(blank=True, null=True)),
                ("aps_check_verification", models.FileField(blank=True, null=True, upload_to="aps_check_verification_uploads")),
                ("hhs_oig_exclusionary_check_verification", models.FileField(blank=True, null=True, upload_to="hhs_oig_exclusionary_check_verification_uploads")),
                ("hhs_oig_exclusionary_check_completed", models.BooleanField(blank=True, default=False, null=True)),
                ("idph_background_check_completed", models.BooleanField(blank=True, default=False, null=True)),
                ("idph_background_check_verification", models.FileField(blank=True, null=True, upload_to="idph_background_check_verification_uploads")),
                ("initial_idph_background_check_completion_date", models.DateField(blank=True, null=True)),
                ("current_idph_background_check_completion_date", models.DateField(blank=True, null=True)),
                ("training_exempt", models.BooleanField(blank=True, default=False, null=True)),
                ("pre_training_verification", models.FileField(blank=True, null=True, upload_to="pretraining_verification_uploads")),
                ("pre_service_completion_date", models.DateField(blank=True, null=True)),
                ("added_to_TTP_portal", models.BooleanField(blank=True, null=True)),
                (
                    "job_title",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("AIDE", "Homecare Aide"),
                            ("CARE_COORDINATOR", "Care Coordinator"),
                            ("CARE_COORDINATOR_SUPERVISOR", "Care Coordinator Supervisor"),
                            ("HOMECARE_SUPERVISOR", "Homecare Supervisor"),
                        ],
                        default="AIDE",
                        max_length=10485760,
                        null=True,
                    ),
                ),
                ("contract_code", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to="compliance.contract")),
            ],
            options={
                "verbose_name": "Compliance-Auditing Data",
                "verbose_name_plural": "Compliance-Auditing Data",
                "db_table": "audit_compliance",
                "ordering": ["employee"],
            },
            bases=(models.Model, django_prometheus.models.ExportModelOperationsMixin("compliance")),
        ),
    ]
