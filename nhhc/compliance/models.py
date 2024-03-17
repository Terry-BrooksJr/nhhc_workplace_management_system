"""
Module: compliance.models

This module defines the Compliance model, which is responsible for storing and managing compliance and auditing data for employees.

Attributes:
    - employee: One-to-one relationship with the Employee model, serving as the primary key and related name for the compliance profile of the employee.
    - aps_check_passed: Boolean field to indicate whether the APS check has been passed.
    - aps_check_verification: FileField to store the verification document for the APS check, using the PrivateMediaStorage()
 for file storage.
    - hhs_oig_exclusionary_check_verification: FileField to store the verification document for the HHS OIG exclusionary check, using the PrivateMediaStorage()
 for file storage.
    - hhs_oig_exclusionary_check_completed: Boolean field to indicate whether the HHS OIG exclusionary check has been completed.
    - idph_background_check_completed: Boolean field to indicate whether the IDPH background check has been completed.
    - idph_background_check_verification: FileField to store the verification document for the IDPH background check, using the PrivateMediaStorage()
 for file storage.
    - initial_idph_background_check_completion_date: DateField to store the initial completion date of the IDPH background check.
    - current_idph_background_check_completion_date: DateField to store the current completion date of the IDPH background check.
    - training_exempt: Boolean field to indicate whether the employee is exempt from training.
    - pre_training_verification: FileField to store the verification document for pre-training, using the PrivateMediaStorage()
 for file storage.
    - pre_service_completion_date: DateField to store the completion date of pre-service activities.
    - added_to_TTP_portal: Boolean field to indicate whether the employee has been added to the TTP portal.
    - contract_code: ForeignKey relationship with the Contract model, allowing for association with a specific contract.
    - job_title: CharField to store the job title of the employee, with predefined choices from the JOB_TITLE class.

Methods:
    - __str__: Returns a formatted string representation of the compliance data, including the employee's last name, first name, and job title.

Meta:
    - db_table: Specifies the name of the database table for the Compliance model.
    - ordering: Specifies the default ordering of records based on the employee field.
    - verbose_name: Specifies the human-readable name for the model in singular and plural forms.

Note: This model utilizes the ExportModelOperationsMixin from django_prometheus for exporting model operations to Prometheus.
"""


from typing import Union

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_prometheus.models import ExportModelOperationsMixin
from employee.models import Employee
from filer.fields.file import FilerFileField
from loguru import logger

from nhhc.backends.storage_backends import PrivateMediaStorage


class Contract(models.Model, ExportModelOperationsMixin("contracts")):
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.code

    class Meta:
        db_table = "contracts"
        ordering = ["code"]
        verbose_name = "State Contract"
        verbose_name_plural = "State Contracts"


class Compliance(models.Model, ExportModelOperationsMixin("compliance")):
    class JOB_TITLE(models.TextChoices):
        AIDE = "AIDE", _("Homecare Aide")
        COORDINATOR = "CARE_COORDINATOR", _("Care Coordinator")
        CC_SUPERVISOR = "CARE_COORDINATOR_SUPERVISOR", _("Care Coordinator Supervisor")
        HC_SUPERVISOR = "HOMECARE_SUPERVISOR", _("Homecare Supervisor")

    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="compliance_profile_of",
    )
    aps_check_passed = models.BooleanField(null=True, blank=True)
    aps_check_verification = models.FileField(
        upload_to="aps_check_verification",
        storage=PrivateMediaStorage(),
        blank=True,
        null=True,
    )
    hhs_oig_exclusionary_check_verification = models.FileField(
        upload_to="hhg-oig", storage=PrivateMediaStorage(), blank=True, null=True
    )
    hhs_oig_exclusionary_check_completed = models.BooleanField(
        null=True,
        blank=True,
        default=False,
    )
    idph_background_check_completed = models.BooleanField(
        null=True,
        blank=True,
        default=False,
    )
    idph_background_check_verification = models.FileField(
        upload_to="idph_bg_check", storage=PrivateMediaStorage(), blank=True, null=True
    )
    initial_idph_background_check_completion_date = models.DateField(
        null=True,
        blank=True,
    )
    current_idph_background_check_completion_date = models.DateField(
        null=True,
        blank=True,
    )
    training_exempt = models.BooleanField(null=True, blank=True, default=False)
    pre_training_verification = models.FileField(
        upload_to="pretraining_verification",
        storage=PrivateMediaStorage(),
        blank=True,
        null=True,
    )
    pre_service_completion_date = models.DateField(null=True, blank=True)
    added_to_TTP_portal = models.BooleanField(null=True, blank=True)
    contract_code = models.ForeignKey(
        Contract, on_delete=models.PROTECT, blank=True, null=True
    )
    job_title = models.CharField(
        null=True,
        choices=JOB_TITLE.choices,
        default=JOB_TITLE.AIDE,
        max_length=255,
        blank=True,
    )

    def __str__(self) -> str:
        return f"Compliance Profile of {self.employee.last_name}, {self.employee.first_name} ({self.employee.pk})"

    def is_eligible_to_work(self) -> bool:
        employee_profile = Employee.objects.get(pk=self.employee.pk)
        # TODO: Implement Miniminally Needed Documentation Check Logic to Determined Ready to Start
        raise NotImplementedError("Logic to Determine This Forth Coming")

    class Meta:
        db_table = "audit_compliance"
        ordering = ["employee"]
        verbose_name = "Compliance-Auditing Data"
        verbose_name_plural = "Compliance-Auditing Data"
