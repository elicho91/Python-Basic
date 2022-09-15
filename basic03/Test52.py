'''
* 공공데이터 *
    www.data.go.kr

    CSV 파일
        Comma-Seperated Values
        형식 : 각 열(colum)은 콤마(,)로 구분, 각 행(row)은 줄바꿈으로 구분
        라이브러리 : csv
'''
import csv
'''
# csv 파일 저장
with open('testCSV.csv', 'w', encoding='utf-8', newline='') as csv_writer:
    writer = csv.writer(csv_writer, delimiter=',')
        #csv 모듈에서 쓰기모드 객체 얻어오기, (파일객체, 구분자)
    writer.writerow(['hello', 'python', 'csv'])
    writer.writerow(['good', 'morning', 1234])
    writer.writerow(['pika']*3 + ['chu'])   #['pika'] * 3 = ['pika','pika','pika']
                                            #['pika','pika','pika'] + ['chu'] = ['pika','pika','pika', 'chu']

# newline '' : 윈도우의 경우 csv 모듈에서 데이터를 쓸때 각 라인 뒤에 빈 라인이 추가되는 문제가 있음
#            이름 없애기 위해 파일 open시 newline을 ''빈 문자열로 지정해줌

# csv 파일 읽기
with open('testCSV.csv', 'r', encoding='utf-8') as csv_reader:
    reader = csv.reader(csv_reader)
    for row in reader:
        print(row)
 '''
# dict 타입으로 저장
with open('testCSV01.csv', 'w', encoding='utf-8', newline='') as csv_writer:
    name_list = ['이름', '주소']
    writer = csv.DictWriter(csv_writer, fieldnames=name_list)
    writer.writeheader()
    writer.writerow({'이름': 'pika', '주소': '서울시 마포구'})
    writer.writerow({'이름': 'raichu', '주소': '서울시 서초구'})
    writer.writerow({'이름': 'kkobugi', '주소': '서울시 관악구'})
    
# dict 타입으로 읽기
with open('testCSV01.csv', 'r', encoding='utf-8') as csv_reader:
    reader = csv.DictReader(csv.reader)
    for row in reader:
        print(row)
        print(row['이름'], row['나이'])

