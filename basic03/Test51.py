'''
데이터 저장
파이썬 - Oracle DB 연동
라이브러리 설치
    - cs-Oracle (pycharm)   cx-oracle(pop install cx_oracle)
    - oracle instant client 다운
'''
import cx_Oracle
import datetime

# 오라클 인스턴트 클라이언트
cx_Oracle.init_oracle_client(lib_dir=r"E:\oracle\instantclient_19_16")
'''
cx_Oracle.connect   : 오라클 커넥션 접속  ('username', 'password', 'url:port/sid')
.cursor             : 쿼리 실행, 결과 데이터 다올 변수 선언
. execute           : SQL 실행, 결과가 cursor에 담김
.fetall             : 쿼리 실행 결과에서 데이터를 한 행씩 fetch 한다.
.description        : 데이터의 컬럼명 추출
'''
conn = cx_Oracle.connect("java06", "java06", "192.168.100.250:1521/orcl")
cursor = conn.cursor()


'''
# 데이터 조회
sql = "select * from test"
cursor.execute(sql) # 쿼리문 실행

for result in cursor:
    # print(result)
    print(result[0])
    print(result[1])
    print(result[2])
    print(result[3])
    print("=" * 50)

# 사용 후 닫기
cursor.close()
conn.close()


# 데이터 저장
import datetime

sql = "insert into test values(:1, :2, :3, :4)"
data = ('py01', '0000', 20, datetime.datetime.now()) # 바인딩시킬 데이터 튜플형태로 만들고
cursor.execute(sql, data)

cursor.close()
conn.commit()
conn.close()


# 데이터 여러개 저장
sql = "insert into test values(:1, :2, :3, :4)"
data = [
    ('py02', '0000', 20, datetime.datetime.now()),
    ('py03', '1111', 30, datetime.datetime.now()),
    ('py04', '2222', 40, datetime.datetime.now()),
    ('py05', '3333', 50, datetime.datetime.now()),
]
cursor.arraysize = len(data)
cursor.executemany(sql, data) # 한번에 여러 레코드 insert

cursor.close()
conn.commit()
conn.close()


# 레코드 개수 수정
sql = "select count(*) from test"
cursor.execute(sql)
count = cursor.fetchone()   # 레코드 한개 추출
print("회원 수 : ", count[0], "명")
cursor.close()
conn.close()


# 데이터 수정
sql = "update test set pw=:1, age=:2 where id=:3"
data = ('9876', 95, 'py01')
cursor.execute(sql, data)

cursor.close()
conn.commit()
conn.close()
'''

# 레코드 삭제
sql = "delete from test where id=:1"
data = ('py01',) # 튜플 형태로 데이터 생성
cursor.execute(sql, data)

cursor.close()
conn.commit()
conn.close()





























