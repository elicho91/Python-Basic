'''
제어문
    조건문 : if
    반복문 : for while
    보조제어문 : continue, break

    for 변수 in 문자열|리스트|튜플:
        실행문들....

    for 변수 in range():
        실행문들...
'''
for i in "hello":
    print(i)

lst = [10,20,30,40,50]
for i in lst:
    print(i)

print("=" * 100)
for i in range(5): # 0 ~ 5 이전까지
    print(i)
    
print("=" * 100)
for i in range(10,15): # (start, end) end 이전까지
    print(i)

print("=" * 100)
for i in range(1,10,2): # (start, end, step) start부터 end 이전까지 step씩 증감
    print(i)

# 구구단 3단 출력
print("=" * 100)
for i in range(1,10): # (start, end) end 이전까지
    print(3, "*", i, "=", (3*i))

# 구구단 전체 출력
print("=" * 100)
for i in range(2,10): # (start, end, step) start부터 end 이전까지 step씩 증감
    print("***", i, "단***")
    for j in range(1, 10):
        print(i, "*", j, "=", (i*j))




