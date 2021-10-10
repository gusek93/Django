import pandas as pd
import warnings

with warnings.catch_warnings(record=True):
    warnings.simplefilter("always")
    df = pd.read_excel(
        "/Users/dayong/project/algorithm/cvstest/cvsdata/부산환경_2019_급여지급현황(전체)_20211001_111035_.xlsx", engine="openpyxl", header=5, usecols="B,G,H,N,Q,U")

data = df.dropna(how='all')
# print(data)
# print(data.shape[0])


test = pd.DataFrame(data)
list_from_df = test.values.tolist()

# print(test.shape[0])
# test.to_excel('test.xlsx')

# 리스트 선언
no_list = []
name_list = []
name_list2 = []
name_list3 = []
name_list4 = []
ssnumber_list = []
jan_list = []
feb_list = []
mar_list = []
apr_list = []
may_list = []
jun_list = []
jul_list = []
aug_list = []
sept_list = []
oct_list = []
nov_list = []
dec_list = []

# 사람 정보가 늘어나는 만큼 값 출력
count = int((test.shape[0]+1)/4)
# print(count)
start = 3
end = count-start


# 1 ~ 3 월 데이터 추출
for i in range(start, end+1):
    no_list.append(list_from_df[i][0])
    name_list.append(list_from_df[i][1])
    ssnumber_list.append(list_from_df[i][2])
    jan_list.append(list_from_df[i][3])
    feb_list.append(list_from_df[i][4])
    mar_list.append(list_from_df[i][5])


# 4 ~ 6 월 데이터 추출
for i in range(count+start, count+end+1):
    apr_list.append(list_from_df[i][3])
    may_list.append(list_from_df[i][4])
    jun_list.append(list_from_df[i][5])


# 7 ~ 9 월 데이터 추출
for i in range(count*2+start, count*2+end+1):
    jul_list.append(list_from_df[i][3])
    aug_list.append(list_from_df[i][4])
    sept_list.append(list_from_df[i][5])


# 10 ~ 12 월 데이터 추출
for i in range(count*3+start, count*3+end+1):
    oct_list.append(list_from_df[i][3])
    nov_list.append(list_from_df[i][4])
    dec_list.append(list_from_df[i][5])


# 추출 데이터 DataFrame으로 변환
no = pd.DataFrame(no_list)
name = pd.DataFrame(name_list)
ssnumber = pd.DataFrame(ssnumber_list)

# 1월 ~ 12 월 데이터
jan = pd.DataFrame(jan_list)
feb = pd.DataFrame(feb_list)
mar = pd.DataFrame(mar_list)

apr = pd.DataFrame(apr_list)
may = pd.DataFrame(may_list)
jun = pd.DataFrame(jun_list)

jul = pd.DataFrame(jul_list)
aug = pd.DataFrame(aug_list)
sept = pd.DataFrame(sept_list)

oct = pd.DataFrame(oct_list)
nov = pd.DataFrame(nov_list)
dec = pd.DataFrame(dec_list)


# 추출 데이터 지정된 컬럼에 정보 넣기
result = pd.concat([no, name, ssnumber, jan, feb, mar, apr,
                   may, jun, jul, aug, sept, oct, nov, dec], axis=1)
result.columns = ["NO", "사원명", "주민번호", "1월", "2월", "3월",
                  "4월", "5월", "6월", "7월", "8월", "9월", "10월", "11월", "12월"]
print(result)

# 엑셀로 변환
# result.to_excel('급여지급현황.xlsx')
