# Generated by Django 5.1.4 on 2024-12-09 23:04

import django.core.validators
import django.db.models.deletion
import django.db.models.deletion
import django_extensions.db.fields
import django_prometheus.models
from django.conf import settings
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):


    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="PayrollException",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("date", models.DateField()),
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
                ("num_hours", models.PositiveIntegerField()),
                ("rejection_reason", models.TextField(blank=True, null=True)),
                ("rejection_reason", models.TextField(blank=True, null=True)),
                ("reason", models.TextField(validators=[django.core.validators.MinLengthValidator(50, "the field must contain at least 50 characters")])),
                ("status", models.CharField(choices=[("P", "Pending - Awaiting Supervisor Review"), ("A", "Approved - Time Amended"), ("R", "Rejected")], default="P", max_length=1)),
                ("date_submitted", django_extensions.db.fields.CreationDateTimeField(auto_now_add=True)),
                ("last_modified", django_extensions.db.fields.ModificationDateTimeField(auto_now=True)),
                ("requesting_employee", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name="requesting_employee", to=settings.AUTH_USER_MODEL)),
                ("reviewer", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name="exception_reviewer", to=settings.AUTH_USER_MODEL)),
                ("requesting_employee", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name="requesting_employee", to=settings.AUTH_USER_MODEL)),
                ("reviewer", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name="exception_reviewer", to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "verbose_name": "Payroll Exception",
                "verbose_name_plural": "Payroll Exceptions",
                "db_table": "payroll_exceptions",
                "ordering": ["-date"],
            },
            bases=(models.Model, django_prometheus.models.ExportModelOperationsMixin("exceptions")),
        ),
    ]
