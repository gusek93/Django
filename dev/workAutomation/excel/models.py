from django.db import models

from excel.views import uploadFile

# Create your models here.


class Document(models.Model):
    title = models.CharField(max_length=200)
    uploadedFile = models.FileField(upload_to="salary/")
    dateTimeOfUpload = models.DateTimeField(auto_now=True)


class SalarySum(models.Model):
    title = models.CharField(max_length=100)
    uploadedFile = models.FileField(upload_to="salarySum/")
    dateTimeOfUpload = models.DateTimeField(auto_now=True)


class SalaryCalculate(models.Model):
    title = models.CharField(max_length=100)
    uploadedFile = models.FileField(upload_to="salaryCalculate/")
    dateTimeOfUpload = models.DateTimeField(auto_now=True)


class EmployeeList(models.Model):
    title = models.CharField(max_length=100)
    uploadedFile = models.FileField(upload_to="employeeList/")
    dateTimeOfUpload = models.DateTimeField(auto_now=True)
