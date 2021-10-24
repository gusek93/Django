from django.http.response import JsonResponse
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
        
<<<<<<< HEAD
=======

>>>>>>> f8b8e9afdd0ef0df52b69a684076ecd612bac078
        if "나누기" == fileTitle:        
            file_path = os.path.abspath("media/paymentDivision/")
            shutil.rmtree(file_path)
            os.mkdir(file_path)

            paymentdivision = models.PaymentDivision(
                title=fileTitle,
                uploadedFile=uploadedFile
            )
            paymentdivision.save()
<<<<<<< HEAD
            #print("시작합니다")
            #payment.payment()
=======
            payment.payment()
>>>>>>> f8b8e9afdd0ef0df52b69a684076ecd612bac078
            

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
<<<<<<< HEAD
            #taxfree.taxfree()
        else:
            data = {
                "error":"파일명 다시 확인"
            }
            JsonResponse(data)
        
=======
            taxfree.taxfree()
>>>>>>> f8b8e9afdd0ef0df52b69a684076ecd612bac078

    return render(request, "excel/upload-file.html")

def transPayment(request):
    payment.payment()
    data = {
        "status":"success"
    }
    return JsonResponse(data)

def transTaxfree(request):
    taxfree.taxfree()
    data = {
        "status":"success"
    }
    return JsonResponse(data)

# def transPayment(request):
#     #request.POST["payment"]
#     payment.payment()
#     data = {
#         "status":"success"
#     }
#     return JsonResponse(data)

def downloadPayment(request):
    file_path = os.path.abspath("media/result/payment/")
    file_name = os.path.basename("media/result/payment/나누기성공.xlsx")
    fs = FileSystemStorage(file_path)
    response = FileResponse(fs.open(file_name, 'rb'),
                            content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = f'attachment; filename="division.xlsx"'

    return response

<<<<<<< HEAD
def downloadTaxfree(request):
    file_path = os.path.abspath("media/result/taxfree/")
    file_name = os.path.basename("media/result/taxfree/빼기성공.xlsx")
=======
def downloadFile(request):
    file_path = os.path.abspath("media/result/")
    file_name = os.path.basename("media/result/12개월나누기.xlsx")
>>>>>>> f8b8e9afdd0ef0df52b69a684076ecd612bac078
    fs = FileSystemStorage(file_path)
    response = FileResponse(fs.open(file_name, 'rb'),
                            content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = f'attachment; filename="Subtraction.xlsx"'

    return response


