'''
 * 조건문 if *
    if 조건식:
        조건 참일 경우 실행할 명령문들...

    if 조건식 :
        명령문들...
    else :
        명령문들...

    if 조건식 :
        명령문들...
    elif 조건식 :
        명령문들...
    elif 조건식 :
        명령문들...
    else :
        명령문들...

'''
num = 10
if num > 10:
    print("10보다 크거나 같다")
elif num <10:
    print("10보다 작다")
else:
    print("10이다.")
print("*" * 10)

# 국어 영어 수학 점수를 입력 받아
# 세 과목의 평균을 학점으로 출력하세요.
# 평균 90이상 "A", 80이상 "B", 70이상 "C", 60이상 "D" 그 이하 "F"

kor = int(input("국어 입력 >> "))
eng = int(input("영어 입력 >> "))
math = int(input("수학 입력 >> "))

avg = (kor + eng + math) / 3

if avg >= 90:
    print("A")
elif avg >= 80:
    print("B")
elif avg >= 70:
     print("C")
elif avg >= 60:
     print("D")
else:
    print("F")





















