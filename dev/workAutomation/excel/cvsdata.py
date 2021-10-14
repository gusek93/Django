from numpy.core.fromnumeric import shape
import pandas as pd
import warnings

# 엑셀 읽어오기
with warnings.catch_warnings(record=True):
    warnings.simplefilter("always")
    df = pd.read_excel(
        "/Users/dayong/project/algorithm/cvstest/cvsdata/급상여_추가_보완.xlsx", engine="openpyxl", header=6, usecols="C,D,E,F,H,J,L")

    # df2 = pd.read_excel(
    #     "/Users/dayong/project/algorithm/cvstest/cvsdata/급상여_추가_보완.xlsx", engine="openpyxl", header=6, usecols="F")


# NaN 데이터 제외한 데이터 출력
data = df.dropna(how='all')
list_from_df = data.values.tolist()

# data2 = df2.dropna(how='all')
# list_from_df2 = df2.values.tolist()

# print(list_from_df2)

# resultlist = []
# for i in range(0, df2.shape[0]):
#     resultlist.append(list_from_df2[i][0])

data.columns = ["코드", "성명", "주민번호", "지급총액", "지급액1", "지급액2", "지급액3"]
result = data.sort_values('코드')

# print(result)
datalist = []
list_df = result.values.tolist()

for i in range(0, result.shape[0]):
    datalist.append()

print(result.shape[0])
# result.to_excel('급상여test.xlsx')
