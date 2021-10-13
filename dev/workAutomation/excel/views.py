from django.db.models.query import QuerySet
from django.shortcuts import render
from . import models
import os
import shutil
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage
# Create your views here.


def uploadFile(request):

    if request.method == "POST":
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]

        if "급상여" == fileTitle:
            file_path = os.path.abspath("media/salaryCalculate/")
            shutil.rmtree(file_path)
            os.mkdir(file_path)

            salarycalculate = models.SalaryCalculate(
                title=fileTitle,
                uploadedFile=uploadedFile
            )
            salarycalculate.save()

        elif "사원명부" == fileTitle:
            file_path = os.path.abspath("media/employeeList/")
            shutil.rmtree(file_path)
            os.mkdir(file_path)

            employeelist = models.EmployeeList(
                title=fileTitle,
                uploadedFile=uploadedFile
            )
            employeelist.save()

        elif "급여지급" == fileTitle:
            file_path = os.path.abspath("media/salarySum/")
            shutil.rmtree(file_path)
            os.mkdir(file_path)

            salarysum = models.SalarySum(
                title=fileTitle,
                uploadedFile=uploadedFile
            )
            salarysum.save()

    return render(request, "excel/upload-file.html")


def downloadFile(request):
    file_path = os.path.abspath("media/result/")
    file_name = os.path.basename("media/result/급여지급현황.xlsx")
    fs = FileSystemStorage(file_path)
    response = FileResponse(fs.open(file_name, 'rb'),
                            content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = f'attachment; filename="salary.xlsx"'

    return response
