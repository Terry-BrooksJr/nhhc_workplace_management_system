"""
Module: employee.views


This module contains views and functions for managing employee information, including hiring, rejecting, and viewing employee details.

Functions:
- send_new_user_credentials(new_user): Sends email notification of user name and password to new employees.
- hire(request): Handles the hiring of applicants and sends new user credentials.
- reject(request): Handles the rejection of applicants.
- employee_roster(request): Renders the employee listing page.
- employee_details(request, pk): Renders the employee details page and allows for editing employee information.

Usage:
To use the functions in this module, import the module and call the desired function with the appropriate parameters.
"""
import csv
import json
import os

from announcements.forms import AnnouncementForm
from announcements.models import Announcements
from compliance.forms import ComplianceForm
from compliance.models import Compliance
from django import template
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import redirect, render, reverse
from django.template import loader
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from employee.forms import EmployeeForm
from employee.models import Employee
from loguru import logger
from web.forms import ClientInterestForm
from web.models import ClientInterestSubmissions, EmploymentApplicationModel
from django.conf import settings

logger.add(
    settings.DEBUG_LOG_FILE, diagnose=True, catch=True, backtrace=True, level="DEBUG"
)
logger.add(
    settings.PRIMARY_LOG_FILE, diagnose=False, catch=True, backtrace=False, level="INFO"
)
logger.add(
    settings.LOGTAIL_HANDLER, diagnose=False, catch=True, backtrace=False, level="INFO"
)


# Create your views here.
def send_new_user_credentials(new_user: Employee, password, username) -> bool:
    """
    Internal Non-Rendering View Function to send email notification of user name and password

    Args:
        new_user: Employee Instance of Employee
        password: str Autogenerated Plaintext Password
        username: str Username for the newly created account

    Returns:
        bool - True of the email was successdfully send. 200  HTTP Status Code if successful or 400  Bad Request if not successful and logs a JSON Error object with details

    """
    try:
        email_from = settings.EMAIL_HOST_USER
        sender_email = os.getenv("NOTIFICATION_SENDER_EMAIL")
        recipient_email = [new_user.email]
        sender_password = os.getenv("EMAIL_ACCT_PASSWORD")
        subject = f"Welcome to Nett Hands - {new_user.first_name}!"
        content = f"Welcome to Nett Hands, Please Login Your New Employee Account at https://www.netthandshome.care/login/ and Complete Onboarding Information in the Personal Information Section:\n Username = {username} \n Password = {password} \n  Welcome to the Family, {new_user.first_name}! \n "
        # send_mail(subject, content, email_from, recipient_email)
        return HttpResponse(
            status=200, content={"status": "SENT", "username": username}
        )
    except Exception as e:
        logger.error(f"Unable to Send New User Credentials...{e}")
        return HttpResponse(
            status=400, content=json.loads({"status": "FAIL", "error": e})
        )


def hire(request: HttpRequest) -> HttpResponse:
    """
    This function is used to hire an applicant based on the provided 'pk' value in the request.

    Args:
    - request (HttpRequest): The HTTP request object containing the 'pk' value.

    Returns:
    - HttpResponse: Returns an HTTP response with a status code indicating the success or failure of the hiring process.
    """
    try:
        pk = request.POST.get("pk")
        logger.debug(f" Recieved Hire Request for pk={pk}")
    except (ValueError, TypeError):
        logger.warning(
            "Bad Request to Hire Applicant, Invaild or NO Applcation PK Submitted"
        )
        return HttpResponse(
            status=400,
            content="Failed to hire applicant. Invalid or no 'pk' value provided in the request.",
        )

    try:
        submission = EmploymentApplicationModel.objects.get(pk=pk)
        logger.debug(
            f"Located Application for New Hire: {submission.last_name}, {submission.first_name}"
        )
    except EmploymentApplicationModel.DoesNotExist:
        logger.error(f"Failed to hire applicant. Employment application not found.")
        return HttpResponse(
            status=400,
            content="Failed to hire applicant. Employment application not found.",
        )

    try:
        hired_user = submission.hire_applicant(request.user)
        logger.debug(f"Created User Account. Returning: {hired_user}")
    except Exception as e:
        logger.error(f"Failed to hire applicant. Error: {e}.")
        return HttpResponse(
            status=400, content=f"Failed to hire applicant. Error: {e}."
        )

    try:
        submission.save()
        send_new_user_credentials(
            new_user=hired_user["user"],
            password=hired_user["plain_text_password"],
            username=hired_user["username"],
        )
        content = f"username: {hired_user['username']},  password: {hired_user['plain_text_password']}"
        return HttpResponse(status=201, content=content)
    except Exception as e:
        logger.exception(f"Failed to send new user credentials. Error: {e}")
        return HttpResponse(
            status=400, content=f"Failed to send new user credentials. Error: {e}"
        )


def reject(request: HttpRequest) -> HttpResponse:
    """
    Ajax Hook that updates EmploymentApplicationModel sets application status to REJECTED

    Args:
        request: HttpRequest  instance of the current request being processed

    Returns:
        HttpResponse - Returns status  code 204 if successful or a 418 and logs error message on failure
    """
    try:
        pk = request.POST.get("pk")
        submission = EmploymentApplicationModel.objects.get(id=pk)
        submission.reject_applicant(request.user)
        submission.save()
        return HttpResponse(status=204)
    except Exception as e:
        logger.error(f"JS AJAX Request Failed - Applicant Not Rejected = {e}")
        return HttpResponse(status=418)


class EmployeeRoster(ListView):
    model = Employee
    queryset = Employee.objects.all().order_by("last_name")
    template_name = "home/employee-listing.html"
    context_object_name = "employees"
    paginate_by = 25


class EmployeeDetail(DetailView):
    model = Employee
    template_name = "home/employee-details.html"
    context_object_name = "employee"


def terminate(request: HttpRequest) -> HttpResponse:
    """
    This function is used to terminates an applicant based on the provided 'pk' value in the request.

    Args:
    - request (HttpRequest): The HTTP request object containing the 'pk' value.

    Returns:
    - HttpResponse: Returns an HTTP response with a status code indicating the success or failure of the hiring process.
    """
    try:
        logger.debug(request.POST)
        pk = request.POST.get("pk")
    except (ValueError, TypeError):
        logger.info(
            "Bad Request to Hire Applicant, Invaild or NO Applcation PK Submitted"
        )
        return HttpResponse(
            status=400,
            content="Failed to terminate applicant. Invalid or no 'pk' value provided in the request.",
        )

    try:
        terminated_employee = Employee.objects.get(id=pk)
    except Employee.DoesNotExist:
        logger.info(f"Failed to hire applicant. Employment application not found.")
        return HttpResponse(
            status=404, content="Failed to terminate applicant. Employee not found."
        )

    try:
        terminated_employee.terminate_employment()
        logger.info(
            f"employment status for {terminated_employee.last_name}, {terminated_employee.first_name} TERMINATED"
        )
        return HttpResponse(status=204)
    except Exception as e:
        logger.exception(f"Failed to hire applicant. Error: {e}.")
        return HttpResponse(
            status=400, content=f"Failed to terminate applicant. Error: {e}."
        )


def employee_details(request, pk):
    if request.user.is_staff:
        context = dict()
        context["data"] = Employee.objects.get(id=pk)
        context["compliance"] = Compliance.objects.get(employee=pk)
        user = context["data"]
        compliance = context["compliance"]

        if request.method == "POST":
            user = Employee.objects.get(id=pk)
            compliance = Compliance.objects.get(employee=pk)
            form = EmployeeForm(
                request.POST,
                request.FILES,
                instance=Employee.objects.get(id=pk),
            )
            if form.has_changed:
                if form.is_valid:
                    form.save()
                    return redirect(reverse("profile"))

        elif request.method == "GET":
            context["compliance"] = Compliance.objects.get(employee=pk)
            context["form"] = EmployeeForm(instance=Employee.objects.get(id=pk))
            return render(
                request=request,
                template_name="home/employee-details.html",
                context=context,
            )
    else:
        raise PermissionDenied()
