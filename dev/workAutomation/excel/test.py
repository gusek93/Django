#from .models import Exceltestdata
# file_path = os.path.abspath("../media/employeeList/")
# # shutil.rmtree(file_path)

# file_name = os.path.basename("../media/employeeList/*")

# # os.remove(file_path)
# os.mkdir(file_path)


import pandas as pd
import warnings
#from models import Exceltestdata

def exceldataRe():
# 엑셀 읽어오기
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        df = pd.read_excel(
                "/Users/dayong/project/algorithm/cvstest/cvsdata/급상여.xlsx", engine="openpyxl")


# NaN 데이터 제외한 데이터 출력
    data = df.dropna(how='all')
    #list_from_df = data.values.tolist()
    return data



# for dbfram in data.itertuples():
#     obj = Exceltestdata.objects.create(
#         code=data.CODE,
#         name=data.NAME,
#         ssnum=data.SSNUM,
#         onemonth=ONE,
#         twomonth=TWO,
#         thmonth=THREE
#     )
#     obj.sava()