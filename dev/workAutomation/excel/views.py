from django.db.models.query import QuerySet
from django.shortcuts import render
from . import models
import os
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage
# Create your views here.


def uploadFile(request):
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]

        # Saving the information in the database
        document = models.Document(
            title=fileTitle,
            uploadedFile=uploadedFile
        )
        document.save()

    documents = models.Document.objects.all()

    return render(request, "excel/upload-file.html", context={
        "files": documents
    })


def downloadFile(request):
    file_path = os.path.abspath("media/result/")
    file_name = os.path.basename("media/result/급여지급현황.xlsx")
    fs = FileSystemStorage(file_path)
    response = FileResponse(fs.open(file_name, 'rb'),
                            content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="saler.xlsx"'

    return response
