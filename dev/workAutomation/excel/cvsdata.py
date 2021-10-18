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
#list_from_df = data.values.tolist()

#print(data.NAME)


# exceltestdata = Exceltestdata(
#     data
# )
# exceltestdata.save()

for dbfram in data.itertuples():
    #print(dbfram)
    obj = Exceltestdata.objects.create(
        code=dbfram.CODE,
        name=dbfram.NAME,
        ssnum=dbfram.SSNUM,
        onemonth=dbfram.ONE,
        twomonth=dbfram.TWO,
        thmonth=dbfram.THREE,
    )
    obj.save()
#print(Exceltestdata.objects.all())

#print(data)
#print(exceldataRe())
#print(dir())

