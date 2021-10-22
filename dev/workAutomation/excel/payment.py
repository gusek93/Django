import os
import sys
import glob
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)) + '/app')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'workAutomation.settings')
import django
django.setup()


import pandas as pd
import warnings

file_path = glob.glob('./media/paymentDivision/*')
list_excel = [file for file in file_path if file.endswith(".xlsx")]
excelpath = list_excel[0]

def payment():
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        df = pd.read_excel(excelpath, engine="openpyxl",header=1,usecols="C,D,E,F")

    print(excelpath)
    #NaN 데이터 제외한 데이터 출력
    data = df.dropna(how='all')
    list_from_df = data.values.tolist()
    division = []

    for i in range(0,data.shape[0]):
        division.append(int(list_from_df[i][3])//12)

    # 1월 ~ 12 월 데이터
    jan = pd.DataFrame(division)
    feb = pd.DataFrame(division)
    mar = pd.DataFrame(division)

    apr = pd.DataFrame(division)
    may = pd.DataFrame(division)
    jun = pd.DataFrame(division)

    jul = pd.DataFrame(division)
    aug = pd.DataFrame(division)
    sept = pd.DataFrame(division)

    oct = pd.DataFrame(division)
    nov = pd.DataFrame(division)
    dec = pd.DataFrame(division)

    division = pd.concat([jan, feb, mar, apr,may, jun, jul, aug, sept, oct, nov, dec], axis=1)
    division.columns = ["1월","2월","3월","4월","5월","6월","7월","8월","9월","10월","11월","12월"]

    data.columns = ["코드","사원명","주민번호","지급액"]

    result = pd.concat([data,division], axis=1)
    print(result)

    result.to_excel('./media/result/payment/나누기성공.xlsx')
    #result.to_excel('./media/result/나누기성공.xlsx')


#payment()