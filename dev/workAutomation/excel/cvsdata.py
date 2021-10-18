import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)) + '/app')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'workAutomation.settings')
import django
django.setup()


import pandas as pd
import warnings

from excel.models import Exceltestdata
#from test import exceldataRe
#import sys
# 엑셀 읽어오기

with warnings.catch_warnings(record=True):
    warnings.simplefilter("always")
    df = pd.read_excel(
        "/Users/dayong/project/algorithm/cvstest/cvsdata/급상여.xlsx", engine="openpyxl")


#NaN 데이터 제외한 데이터 출력
data = df.dropna(how='all')


# 엑셀 데이터 db insert
# for dbfram in data.itertuples():
#     #print(dbfram)
#     obj = Exceltestdata.objects.create(
#         code=dbfram.CODE,
#         name=dbfram.NAME,
#         ssnum=dbfram.SSNUM,
#         onemonth=dbfram.ONE,
#         twomonth=dbfram.TWO,
#         thmonth=dbfram.THREE,
#     )
#     obj.save()


# db 데이터 엑셀 insert
obj = Exceltestdata.objects.all().values_list()
resultdata = []
for i in obj:
    resultdata.append(i)

result = pd.DataFrame(resultdata)
result.columns = ["NO","코드","사원명","주민번호","1월","2월","3월"]
print(result)

result.to_excel('../media/result/dbDataExcel.xlsx')