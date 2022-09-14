'''
1. 출력문
    print()
    * 연결하여 출력
    문자 + 문자 : 문자 연결되어 출력
    문자, 문자 : 띄어쓰기되어 출력
    숫자 + 숫자 : 연산 결과 출력
    숫자, 숫자 :  나란히 출력
    문자, 숫자 : 나란히 출력
    문자 + 숫자 : 에러~!!
    문자 * 숫자 : 문자가 숫자만큼 반복되서 출력

'''
from builtins import type

print(10)
print("hello")
print("hello2")

# print("10" + 10)
print("문자", "문자2")
print("문자" + "문자2")
print(10, 10)
print("hello" * 10)

print("엔터기능 없애기", end=" ")
print("다음줄에 출력????")

'''
* 이스케이프 문자 *
    \n : 줄바꿈
    \t : 탭간격
    \' : 홑따옴표 문자로 출력
    \" : 겹따옴표 문자로 출력
'''
print("내\t이름은\"피카츄\"입니다.")
name = "뽀로로"
age = 10
print("내 이름은", name, "입니다.")
# 서식문자 : 정수 %d, 실수 %f, 문자열 %s
print("내 이름은 %s 입니다. 나이는 %d 살입니다." % (name, age))
# format
print("내 이름은 {} 입니다. 나이는 {} 살입니다.".format(name, age))

'''
 * 데이터 타입 *
    1) 숫자형
        정수      int (python 3.x)    int, long(python 2.x)
        실수      float (python 3.x) 5000/3 = 1666.66666
                        (python 2.x) 5000/3 = 1666  
    2) 참/거짓형
        bool    True / False
    3) 군집자료형
        문자열형  : str 
        리스트    : list
        튜플      : tuple
        딕셔너리  : dict
        집합      : set
        

 * 변수 variable *
    변수명 = 값
    
    type(값/변수) : 데이터 타입 확인 가능
    
    변수명명 규칙
        숫자로 시작X, 대소문자 구분 num Num
        특수기호는 _ (밑줄)만 허용
        keyword 사용불가
'''
print("*" * 50)
num = 10
print(num)
print(type(num))
print(id(num))
num2 = 2.14
print(num2)

hello = "안녕하세요"
print(hello)

'''
 * 입력문 *
    : 콘솔을 통해서 값 입력. 문자열로 리턴
    변수 = input("콘솔에 띄울 메세지") 
    
 * 형변환 casting, convert *
    문자 -----> int
        int(값)
    문자 -----> float
        float(값)
    int, float -----> 문자
                str(값)
'''

print("*" * 50)
#
# print(msg)msg = input("메세지 입력 >>")
age = int(input("나이 입력 >> "))
print(age + 1)
