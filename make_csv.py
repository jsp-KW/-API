import requests
import csv

#url을 통하여 json 형식의 데이터를 받아온다.
def get_json_data(url) :
    response = requests.get(url)
    data = response.json()
    return data


#json 데이터를 csv 파일로 저장하는 함수

def json_to_csv (data, filename) :

    data_list =[]
    #json데이터에서 원하는 data를 추가.
    
    get_info = ['ITEM_NAME1', 'TIME', 'DATA_VALUE']

    for item in data['StatisticSearch']['row'] :
        row_data = [item[info] for info in get_info] 
        data_list.append(row_data)

    with open (filename, 'w',  newline='',encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerows(data_list)

#url 예시
#https://ecos.bok.or.kr/api/StatisticSearch/sample/xml/kr/1/10/722Y001/M/202101/202306/0101000


service_name = "StatisticSearch"
key = "" #api 인증키 
data_type =  "json"
language= "kr"
request_start = "1"
request_finish = "36"
get_data_time = "M" #검색주기가 바뀌면 검색시작일과 검색종료일의 입력형식 또한 달라짐!
search_first_time = "202001"
search_second_time = "202212"
table = "722Y001" #통계표코드
item = "0101000"

url = "https://ecos.bok.or.kr/api/" + service_name + "/" + key + "/" + data_type + "/" + language + "/" + request_start + "/" + request_finish + "/" + table + "/" + get_data_time + "/" + search_first_time + "/" + search_second_time + "/" + item


data = get_json_data (url)

print ("url 을 호출하여 api를 통해 받아온 데이터를 출력해봅니다.")
print (data)

print ("받아온 json 형식의 데이터를 가져와서 csv 파일에 원하는 데이터 정보만 추출하여 저장하겠습니다.")
json_to_csv (data,"한국은행금리.csv")