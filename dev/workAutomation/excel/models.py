from django.db import models

# Create your models here.


class Document(models.Model):
    title = models.CharField(max_length=200)
    uploadedFile = models.FileField(upload_to="salary/")
    dateTimeOfUpload = models.DateTimeField(auto_now=True)


class TaxfreeSubtraction(models.Model):
    title = models.CharField(max_length=100)
    uploadedFile = models.FileField(upload_to="taxfreeSubtraction/")
    dateTimeOfUpload = models.DateTimeField(auto_now=True)


class PaymentDivision(models.Model):
    title = models.CharField(max_length=100)
    uploadedFile = models.FileField(upload_to="paymentDivision/")
    dateTimeOfUpload = models.DateTimeField(auto_now=True)


class EmployeeList(models.Model):
    title = models.CharField(max_length=100)
    uploadedFile = models.FileField(upload_to="employeeList/")
    dateTimeOfUpload = models.DateTimeField(auto_now=True)


class Exceltestdata(models.Model):
    code = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    ssnum = models.CharField(max_length=500)
    onemonth = models.CharField(max_length=500, null=True)
    twomonth = models.CharField(max_length=500, null=True)
    thmonth = models.CharField(max_length=500, null=True)
