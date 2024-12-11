# Generated by Django 5.1.4 on 2024-12-09 23:04

import django.db.models.deletion
import django_extensions.db.fields
import django_prometheus.models
import localflavor.us.models
import nhhc.utils.upload
import phonenumber_field.modelfields
import sage_encrypt.fields.asymmetric
from django.conf import settings
from django.contrib.postgres.operations import CryptoExtension
from django.db import migrations, models

import nhhc.utils.upload
from django.contrib.postgres.operations import CryptoExtension


class Migration(migrations.Migration):


    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        CryptoExtension(),
        migrations.CreateModel(
            name="ClientInterestSubmission",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("first_name", sage_encrypt.fields.asymmetric.EncryptedCharField(max_length=10485760)),
                ("last_name", sage_encrypt.fields.asymmetric.EncryptedCharField(max_length=10485760)),
                ("email", sage_encrypt.fields.asymmetric.EncryptedEmailField(max_length=254, null=True)),
                ("contact_number", phonenumber_field.modelfields.PhoneNumberField(max_length=128, region="US")),
                ("home_address1", sage_encrypt.fields.asymmetric.EncryptedCharField(max_length=800, null=True)),
                ("home_address2", sage_encrypt.fields.asymmetric.EncryptedCharField(blank=True, max_length=50, null=True)),
                ("city", sage_encrypt.fields.asymmetric.EncryptedCharField(blank=True, max_length=10485760, null=True)),
                ("zipcode", localflavor.us.models.USZipCodeField(blank=True, max_length=10, null=True)),
                ("state", localflavor.us.models.USStateField(blank=True, max_length=2, null=True)),
                ("insurance_carrier", sage_encrypt.fields.asymmetric.EncryptedCharField(max_length=10485760)),
                (
                    "desired_service",
                    sage_encrypt.fields.asymmetric.EncryptedCharField(
                        choices=[
                            ("I", "Intermittent Home Care"),
                            ("NM", "Non-Medical Home Care"),
                            ("MSW", "Medical Social Work"),
                            ("OT", "Occupational Therapy"),
                            ("PT", "Physical Therapy"),
                            ("NA", "Other"),
                        ],
                        max_length=10485760,
                    ),
                ),
                ("date_submitted", django_extensions.db.fields.CreationDateTimeField(auto_now_add=True)),
                ("reviewed", models.BooleanField(blank=True, db_index=True, default=False, null=True)),
                ("last_modified", django_extensions.db.fields.ModificationDateTimeField(auto_now=True)),
                ("reviewed_by", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "verbose_name": "Interested Client",
                "verbose_name_plural": "Interested Clients",
                "db_table": "interest_clients",
                "ordering": ["last_name", "first_name", "date_submitted"],
            },
            bases=(models.Model, django_prometheus.models.ExportModelOperationsMixin("client_inquiries")),
        ),
        migrations.CreateModel(
            name="EmploymentApplicationModel",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("first_name", sage_encrypt.fields.asymmetric.EncryptedCharField(max_length=10485760)),
                ("last_name", sage_encrypt.fields.asymmetric.EncryptedCharField(max_length=10485760)),
                ("contact_number", phonenumber_field.modelfields.PhoneNumberField(max_length=128, region="US")),
                ("email", sage_encrypt.fields.asymmetric.EncryptedEmailField(max_length=10485760)),
                ("home_address1", sage_encrypt.fields.asymmetric.EncryptedCharField(max_length=10485760)),
                ("home_address2", sage_encrypt.fields.asymmetric.EncryptedCharField(blank=True, max_length=10485760, null=True)),
                ("city", sage_encrypt.fields.asymmetric.EncryptedCharField(max_length=10485760)),
                ("state", localflavor.us.models.USStateField(max_length=2)),
                ("zipcode", localflavor.us.models.USZipCodeField(max_length=10)),
                (
                    "mobility",
                    models.CharField(
                        choices=[
                            ("C", "I Have Consistent Access To A Car"),
                            ("P", "I Use Public Transportation"),
                            ("RS", "I Use Rideshare (Uber/Lyft) or a Reliable Pickup/Dropoff Provider"),
                            ("NA", "Other"),
                        ],
                        max_length=10485760,
                    ),
                ),
                ("prior_experience", models.CharField(choices=[("S", "12+ Months"), ("J", "3+ Months"), ("N", "No Prior Experience")], max_length=10485760)),
                ("ipdh_registered", models.BooleanField(default=False)),
                ("availability_monday", models.BooleanField(blank=True, null=True)),
                ("availability_tuesday", models.BooleanField(blank=True, null=True)),
                ("availability_wednesday", models.BooleanField(blank=True, null=True)),
                ("availability_thursday", models.BooleanField(blank=True, null=True)),
                ("availability_friday", models.BooleanField(blank=True, null=True)),
                ("availability_saturday", models.BooleanField(blank=True, null=True)),
                ("availability_sunday", models.BooleanField(blank=True, null=True)),
                ("reviewed", models.BooleanField(blank=True, db_index=True, default=False, null=True)),
                ("hired", models.BooleanField(blank=True, null=True)),
                ("date_submitted", django_extensions.db.fields.CreationDateTimeField(auto_now_add=True)),
                ("last_modified", django_extensions.db.fields.ModificationDateTimeField(auto_now=True)),
                ("employee_id", models.BigIntegerField(blank=True, null=True)),
                ("resume_cv", models.FileField(blank=True, null=True, upload_to=nhhc.utils.upload.UploadHandler.generate_randomized_file_name)),
                ("reviewed_by", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "verbose_name": "Prospective Employee",
                "verbose_name_plural": "Prospective Employees",
                "db_table": "employment_interests",
                "ordering": ["last_name", "first_name", "date_submitted"],
            },
            bases=(models.Model, django_prometheus.models.ExportModelOperationsMixin("applications")),
        ),
    ]
