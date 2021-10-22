from django.shortcuts import render

#from excel.taxfree import taxfree
from . import models, payment, taxfree
import os
import shutil
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.


def uploadFile(request):

    if request.method == "POST":
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]
        

        if "나누기" == fileTitle:        
            file_path = os.path.abspath("media/paymentDivision/")
            shutil.rmtree(file_path)
            os.mkdir(file_path)

            paymentdivision = models.PaymentDivision(
                title=fileTitle,
                uploadedFile=uploadedFile
            )
            paymentdivision.save()
            payment.payment()
            

        elif "사원명부" == fileTitle:
            file_path = os.path.abspath("media/employeeList/")
            shutil.rmtree(file_path)
            os.mkdir(file_path)

            employeelist = models.EmployeeList(
                title=fileTitle,
                uploadedFile=uploadedFile
            )
            employeelist.save()

        elif "빼기" == fileTitle:
            file_path = os.path.abspath("media/taxfreeSubtraction/")
            shutil.rmtree(file_path)
            os.mkdir(file_path)

            taxfreeSubtraction = models.TaxfreeSubtraction(
                title=fileTitle,
                uploadedFile=uploadedFile
            )
            taxfreeSubtraction.save()
            taxfree.taxfree()

    return render(request, "excel/upload-file.html")


def downloadFile(request):
    file_path = os.path.abspath("media/result/")
    file_name = os.path.basename("media/result/12개월나누기.xlsx")
    fs = FileSystemStorage(file_path)
    response = FileResponse(fs.open(file_name, 'rb'),
                            content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = f'attachment; filename="salary.xlsx"'

    return response


