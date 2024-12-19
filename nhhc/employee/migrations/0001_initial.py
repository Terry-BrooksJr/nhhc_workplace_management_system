# Generated by Django 5.1.4 on 2024-12-18 20:24

import django_extensions.db.fields
import django_prometheus.models
import employee.models
import localflavor.us.models
import nhhc.utils.upload
import phonenumber_field.modelfields
import sage_encrypt.fields.asymmetric
from django.db import migrations, models

from django.contrib.postgres.operations import CryptoExtension


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [CryptoExtension(),
        migrations.CreateModel(
            name="Employee",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
                ("is_superuser", models.BooleanField(default=False, help_text="Designates that this user has all permissions without explicitly assigning them.", verbose_name="superuser status")),
                ("is_staff", models.BooleanField(default=False, help_text="Designates whether the user can log into this admin site.", verbose_name="staff status")),
                (
                    "is_active",
                    models.BooleanField(default=True, help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.", verbose_name="active"),
                ),
                ("employee_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("username", models.CharField(db_index=True, max_length=150)),
                (
                    "gender",
                    sage_encrypt.fields.asymmetric.EncryptedCharField(
                        blank=True, choices=[("M", "Male"), ("F", "Female"), ("X", "Non-Gendered"), ("B", "Binary")], default="X", max_length=10485760, null=True
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("ENGLISH", "English"),
                            ("CHINESE", "Ethnic Chinese"),
                            ("GREEK", "Greek"),
                            ("ITALIAN", "Italian"),
                            ("LAOTIAN", "Laotian"),
                            ("ROMANIAN", "Romanian"),
                            ("TAGALOG", "Tagalog"),
                            ("YIDDISH", "Yiddish"),
                            ("ARABIC", "Arabic"),
                            ("FARSI", "Farsi"),
                            ("GUJARATI", "Gujarati"),
                            ("JAPANESE", "Japanese"),
                            ("LITHUANIAN", "Lithuanian"),
                            ("RUSSIAN", "Russian"),
                            ("UKRANIAN", "Ukranian"),
                            ("YUGOSLAVIAN", "Yugoslavian"),
                            ("ASSYRIAN", "Assyrian"),
                            ("FRENCH", "French"),
                            ("CREOLE", "Haitian Creole"),
                            ("MON-KHMER", "Mon-Khmer"),
                            ("MANDARIN", "Mandarin"),
                            ("SPANISH", "Spanish"),
                            ("URDU", "Urdu"),
                            ("CANTONESE", "Cantonese"),
                            ("GERMAN", "German"),
                            ("HINDI", "Hindi"),
                            ("KOREAN", "Korean"),
                            ("POLISH", "Polish"),
                            ("SWEDISH", "Swedish"),
                            ("VIETNAMESE", "Vietnamese"),
                        ],
                        default="ENGLISH",
                        max_length=10485760,
                        null=True,
                    ),
                ),
                ("email", sage_encrypt.fields.asymmetric.EncryptedEmailField(blank=True, max_length=254, null=True, unique=True)),
                ("social_security", sage_encrypt.fields.asymmetric.EncryptedCharField(blank=True, null=True, unique=True)),
                ("date_of_birth", sage_encrypt.fields.asymmetric.EncryptedDateField(blank=True, null=True)),
                ("first_name", sage_encrypt.fields.asymmetric.EncryptedCharField(blank=True, max_length=10485760, null=True)),
                ("middle_name", sage_encrypt.fields.asymmetric.EncryptedCharField(blank=True, max_length=10485760, null=True)),
                ("last_name", sage_encrypt.fields.asymmetric.EncryptedCharField(blank=True, max_length=10485760, null=True)),
                ("street_address1", sage_encrypt.fields.asymmetric.EncryptedCharField(blank=True, max_length=10485760, null=True)),
                ("street_address2", sage_encrypt.fields.asymmetric.EncryptedCharField(blank=True, max_length=10485760, null=True)),
                (
                    "marital_status",
                    models.CharField(
                        blank=True, choices=[("M", "Married"), ("D", "Divorced"), ("S", "Separated"), ("W", "Widowed"), ("NM", "Never Married")], default="NM", max_length=10485760, null=True
                    ),
                ),
                ("emergency_contact_first_name", sage_encrypt.fields.asymmetric.EncryptedCharField(blank=True, max_length=10485760, null=True)),
                ("emergency_contact_last_name", sage_encrypt.fields.asymmetric.EncryptedCharField(blank=True, max_length=10485760, null=True)),
                (
                    "race",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("BLACK", "Black/African American"),
                            ("NATIVE", "American Indian/Alaska Native"),
                            ("ASIAN", "Asian"),
                            ("HAWAIIAN", "Native Hawaiian/Other Pacific Islander"),
                            ("WHITE", "White/Caucasian"),
                            ("OTHER", "Other Race"),
                            ("BI_RACIAL", "Two or More Races"),
                            ("UNKNOWN", "Unknown"),
                            ("REFUSED", "Perfer Not To Disclose"),
                        ],
                        default="UNKNOWN",
                        max_length=10485760,
                        null=True,
                    ),
                ),
                ("emergency_contact_relationship", sage_encrypt.fields.asymmetric.EncryptedCharField(blank=True, max_length=10485760, null=True)),
                ("emergency_contact_phone", phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region="US")),
                ("city", sage_encrypt.fields.asymmetric.EncryptedCharField(blank=True, max_length=10485760, null=True)),
                ("idoa_agency_policies_attestation", models.FileField(blank=True, default="NONE", upload_to="idoa_agency_policies")),
                ("dhs_i9", models.FileField(blank=True, default="NONE", upload_to="i9")),
                ("marketing_recruiting_limitations_attestation", models.FileField(blank=True, default="NONE", upload_to="marketing_recruiting_limitations")),
                ("do_not_drive_agreement_attestation", models.FileField(blank=True, default="NONE", upload_to="do_not_drive_agreement")),
                ("job_duties_attestation", models.FileField(blank=True, default="NONE", upload_to="job_duties")),
                ("hca_policy_attestation", models.FileField(blank=True, default="NONE", upload_to="hca_policy")),
                ("irs_w4_attestation", models.FileField(blank=True, default="NONE", upload_to="irs_w4")),
                ("state_w4_attestation", models.FileField(blank=True, default="NONE", upload_to="state_w4")),
                ("idph_background_check_authorization", models.FileField(blank=True, default="NONE", upload_to="idph_bg_check_auth")),
                ("qualifications_verification", models.FileField(blank=True, default="NONE", upload_to=nhhc.utils.upload.UploadHandler("resume"))),
                ("cpr_verification", models.FileField(blank=True, default="NONE", upload_to=nhhc.utils.upload.UploadHandler("cpr_verification"))),
                (
                    "family_hca",
                    models.CharField(
                        blank=True, choices=[("true", "Yes, I am Related to my patient"), ("false", "No, I am NOT Related to my patient")], default="false", max_length=10485760, null=True
                    ),
                ),
                ("phone", phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
                ("state", localflavor.us.models.USStateField(max_length=2, null=True)),
                (
                    "ethnicity",
                    models.CharField(
                        blank=True,
                        choices=[("NON-HISPANIC", "Non-Hispanic/Latino"), ("HISPANIC", "Hispanic/Latino"), ("UNKNOWN", "Unknown"), ("REFUSED", "Perfer Not To Disclose")],
                        max_length=10485760,
                        null=True,
                    ),
                ),
                ("sms_contact_agreement", models.BooleanField(help_text="Please Confirm that You Agree to the SMS Communication ", null=True)),
                ("sms_contact_number", phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
                ("zipcode", localflavor.us.models.USZipCodeField(max_length=10, null=True)),
                ("application_id", models.BigIntegerField(blank=True, null=True, unique=True)),
                ("hire_date", django_extensions.db.fields.CreationDateTimeField(auto_now_add=True)),
                ("termination_date", models.DateField(blank=True, null=True)),
                (
                    "qualifications",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("HIGH_SCHOOL_GED", "High School Diploma/GED"),
                            ("CNA", "Certified Nursing Assistant (CNA)"),
                            ("LPN", "LPN"),
                            ("RN", "Registered Nurse (RN)"),
                            ("EXPERIENCE", "Applicable Experience"),
                            ("BACHELORS", "Bachelor's degree"),
                            ("MASTERS", "Master’s degree and above"),
                            ("O", "Other"),
                        ],
                        default="HIGH_SCHOOL_GED",
                        max_length=10485760,
                        null=True,
                    ),
                ),
                ("_date_joined", django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, db_column="date_joined")),
                ("last_modifed", django_extensions.db.fields.ModificationDateTimeField(auto_now=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True, help_text="Specific permissions for this user.", related_name="user_set", related_query_name="user", to="auth.permission", verbose_name="user permissions"
                    ),
                ),
            ],
            options={
                "verbose_name": "Agency Employee",
                "verbose_name_plural": "Agency Employees",
                "db_table": "employee",
                "ordering": ["last_name", "first_name", "-hire_date"],
                "get_latest_by": "-hire_date",
                "indexes": [models.Index(fields=["username"], name="username_idx"), models.Index(fields=["first_name"], name="first_name_idx")],
            },
            bases=(employee.models.EmployeeMethodUtility, models.Model, django_prometheus.models.ExportModelOperationsMixin("employee")),
        ),
    ]
