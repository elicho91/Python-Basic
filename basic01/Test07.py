'''
제어문
    조건문 : if
    반복문 : for while
    보조제어문 : continue, break

* 반복문 while *
    whlie 조건식 :
        반복문 실행문들...

    while True :
        실행문들...
        if 조건식: break   * 종료 시점 필요 *

'''
i = 0
while i < 10:  # 조건식
    print(i)
    i += 1  #  증가식

# 1~10 까지의 짝수를 모두 더한 값 출력
total = 0
i = 1
while i <= 10:
    if i % 2 == 0:
        total += i
    i += 1
print("총합 : ", total)

print("=" * 100)

while True:
    num = int(input("숫자입력 : "))
    print(num)
    if num == 9:
        break
print("while true 종료!!")