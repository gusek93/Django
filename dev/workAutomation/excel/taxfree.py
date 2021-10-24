import os
import sys
import glob
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)) + '/app')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'workAutomation.settings')
import django
django.setup()

import pandas as pd
import warnings

# 엑셀 읽어오기
file_path = glob.glob('./media/taxfreeSubtraction/*')
list_excel = [file for file in file_path if file.endswith(".xlsx")]



def taxfree():
    excelpath = list_excel[0]
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        df = pd.read_excel(excelpath, engine="openpyxl",usecols="A,B,E,F,I")

    list_from_df = df.values.tolist()
    data = df.dropna(how='all')

    num_list = []   
    name_list = []
    sal_list = []
    car_list = []
    run_list = []
    salcaculater = []
    salcaculater2 = []

    i = 0
    while i < len(data):
        num_list.append(list_from_df[i][0])
        name_list.append(list_from_df[i][1])
        car_list.append(list_from_df[i][2])
        run_list.append(list_from_df[i][3])
        salcaculater.append(list_from_df[i][2] - list_from_df[i][3])
        i += 3


    j = 2
    x = 0
    while j< len(data):
        
        sal_list.append(list_from_df[int(j)][4])
        salcaculater2.append(list_from_df[int(j)][4] - salcaculater[x])
        j += 3
        x +=1
 

    num_list_data = pd.DataFrame(num_list)
    name_list_data = pd.DataFrame(name_list)
    car_list_data = pd.DataFrame(car_list)
    run_list_data = pd.DataFrame(run_list)
    sal_list_data = pd.DataFrame(sal_list)
    salcaculater2 = pd.DataFrame(salcaculater2)
    
    result = pd.concat([num_list_data,name_list_data,car_list_data,run_list_data,sal_list_data,salcaculater2], axis=1)
    result.columns = ["사원번호","사원명","차량유지비","식대","급여","결과"]
    print(result)
    
    
    #df.to_excel('../media/result/계산성공.xlsx')
    result.to_excel('./media/result/taxfree/빼기성공.xlsx')
    #print(num_list,name_list,car_list,run_list)

#taxfree()