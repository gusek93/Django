import os
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage

# print(os.getcwd())
# print(os.path.abspath("../media/result"))


def downloadFile():
    file_dir = os.path.abspath("media/result/")
    file_name = os.path.basename("media/result/급상여지급현황.xlsx")
    fs = FileSystemStorage(file_dir)
    response = FileResponse(fs.open(file_dir, 'rb'))
    response['Content-Disposition'] = f'attachment; filename={file_name}'

    return response


downloadFile()
