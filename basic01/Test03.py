'''
 * 문자열  str*
    "문자열" '문자열 """여러줄문자열""" (홑따옴표도 가능)

    1) 인덱스
        0 ~ 시작하는 인덱스 번호
    2) 인덱싱
    3) 특징
        수정 불가능함 immutable
    4) 슬라이싱
        문자열[시작인덱스:끝인덱스] 끝인덱스번호 전까지 잘라줌
'''
str1 = "hello"
print(str1[-1])
print(str1[0 : 2])
print(str1[2:4])

str2 = "TheJoeun Institute"
# TheJoeun 만 출력
print(str2[:8])
# Institute만 출력
print(str2[9:])
str3 = "prigraming"
# 문제3. programing으로 변경해서 출력
print(str3[:2]+"o"+str3[3:7]+"m"+str3[-3:])
str3="programming"
print(str3)

# 날짜 잘라보기
import datetime
today = datetime.date.today()
print(today)
print(type(today))
#print(today[:4])
today = str(today)
print(today[:4])

# 문자열 관련 함수
str4 = "hello python~!"
print(str4)
str4 = str4.replace("python", "pycharm")
print(str4)
# split() : 문자열 나누기
# result = str4.split()   # 공백 기준으로 나눠줌
result = "hello:hahahahaha".split(":")
print(result)
# len() : 문자열 길이
str5 = "fedfawregasregasdgasdzf"
print(len(str5))
print(str5.count('f'))
name = "thejoeun"
# find() : 문자 인덱스 알아내기
print(name.find('e'))
print(name.find('z')) # 없는 문자는 -1로 리턴
# index() : 문자 인덱스 알아내기
print(name.index('j'))
# print(name.index('z')) # 에러발생

# 소문자/대문자로 리턴 : lower(), upper()
str5 = "Apple Tree"
print(str5.lower())
print(str5.upper())

# 공백 지우기 : strip(), lstrip(), rstrip()
str6 = "        python          "
print(str6)
print(str6.strip()) # 앞뒤 공백 삭제
print(str6.lstrip()) # 왼쪽 공백 삭제
print(str6.rstrip()) # 오른쪽 공백 삭제
