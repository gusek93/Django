from django.db import models

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


class Exceltestdata(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    ssnum = models.CharField(max_length=300)
    onemonth = models.CharField(max_length=200, null=True)
    twomonth = models.CharField(max_length=200, null=True)
    thmonth = models.CharField(max_length=200, null=True)
