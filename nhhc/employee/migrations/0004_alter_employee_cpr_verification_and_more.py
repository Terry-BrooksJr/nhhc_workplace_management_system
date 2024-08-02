# Generated by Django 5.0.6 on 2024-07-31 03:25

from django.db import migrations, models

import nhhc.utils.upload


class Migration(migrations.Migration):
    dependencies = [
        ("employee", "0003_alter_employee_dhs_i9_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="cpr_verification",
            field=models.FileField(blank=True, default="NONE", upload_to=nhhc.utils.upload.UploadHandler("cpr_verification")),
        ),
        migrations.AlterField(
            model_name="employee",
            name="dhs_i9",
            field=models.FileField(blank=True, default="NONE", upload_to="i9"),
        ),
        migrations.AlterField(
            model_name="employee",
            name="do_not_drive_agreement_attestation",
            field=models.FileField(blank=True, default="NONE", upload_to="do_not_drive_agreement"),
        ),
        migrations.AlterField(
            model_name="employee",
            name="hca_policy_attestation",
            field=models.FileField(blank=True, default="NONE", upload_to="hca_policy"),
        ),
        migrations.AlterField(
            model_name="employee",
            name="idoa_agency_policies_attestation",
            field=models.FileField(blank=True, default="NONE", upload_to="idoa_agency_policies"),
        ),
        migrations.AlterField(
            model_name="employee",
            name="idph_background_check_authorization",
            field=models.FileField(blank=True, default="NONE", upload_to="idph_bg_check_auth"),
        ),
        migrations.AlterField(
            model_name="employee",
            name="irs_w4_attestation",
            field=models.FileField(blank=True, default="NONE", upload_to="irs_w4"),
        ),
        migrations.AlterField(
            model_name="employee",
            name="job_duties_attestation",
            field=models.FileField(blank=True, default="NONE", upload_to="job_duties"),
        ),
        migrations.AlterField(
            model_name="employee",
            name="marketing_recruiting_limitations_attestation",
            field=models.FileField(blank=True, default="NONE", upload_to="marketing_recruiting_limitations"),
        ),
        migrations.AlterField(
            model_name="employee",
            name="qualifications_verification",
            field=models.FileField(blank=True, default="NONE", upload_to=nhhc.utils.upload.UploadHandler("resume")),
        ),
        migrations.AlterField(
            model_name="employee",
            name="state_w4_attestation",
            field=models.FileField(blank=True, default="NONE", upload_to="state_w4"),
        ),
    ]