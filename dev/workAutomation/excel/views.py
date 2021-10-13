from django.db.models.query import QuerySet
from django.shortcuts import render
from . import models
import os
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage
# Create your views here.


def uploadFile(request):
    # print("hi")
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]

        # print(uploadedFile)
        if "급상여" == fileTitle:
            salarycalculate = models.SalaryCalculate(
                title=fileTitle,
                uploadedFile=uploadedFile
            )
            salarycalculate.save()

        elif "사원명부" == fileTitle:
            employeelist = models.EmployeeList(
                title=fileTitle,
                uploadedFile=uploadedFile
            )
            employeelist.save()

        elif "급여지급" == fileTitle:
            salarysum = models.SalarySum(
                title=fileTitle,
                uploadedFile=uploadedFile
            )
            salarysum.save()

            models.SalaryCalculate.objects.all()
            models.EmployeeList.objects.all()
            models.SalarySum.objects.all()

    return render(request, "excel/upload-file.html")


def downloadFile(request):
    file_path = os.path.abspath("media/result/")
    file_name = os.path.basename("media/result/급여지급현황.xlsx")
    fs = FileSystemStorage(file_path)
    response = FileResponse(fs.open(file_name, 'rb'),
                            content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = f'attachment; filename="salary.xlsx"'

    return response
