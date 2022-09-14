'''
군집 자료형 : 문자형 str, list, tuple, dict, set
 * 리스트 list *
    여러 데이터 한번에 저장.
    다양한 데이터 타입을 섞어서 저장가능
    수정 가능 mutable
    크기 제한 없다.
    구분기호 : []
'''
a = [] # 빈 리스트
b = list() # 빈 리스트
print(b)
print(type(b))
c = [1,2,3,4,5]
print(c)
d = [1, 2, True, "hello", "python", [10,20,30]]
print(d)
print(d[-1][-2])

lst = [1,2,3,[4,5,6],7]
# 숫자 4 출력
print(lst[-2][-3])
# 숫자 3 출력
print(lst[-3])
# 숫자 7 출력
print(lst[-1])

lst2 = [1,2,3,["a","b","c"],4,5]
# [3,["a","b","c"],4] 출력
print(lst2[2:-1])
#["a","b"] 출력
print(lst2[3][:2])

# 값 수정
lst = [1,2,3]
lst[0] = 100
print(lst)

lst = [1,2,3,4,5]
# 인덱스번호 1번의 요소를 'a', 'b', 'c'로 수정해보자
# lst[1] = ['a','b','c']
# print(lst)
# lst[1:2] = ['a','b','c']
print(lst)
lst[1] = 'a','b','c' # 튜플
print(lst)

# 리스트 관련 함수
#1. 요소 추가 : append()
lst3 = []
print(lst3)
lst3.append(10)
lst3.append(20)
print(lst3)

#2. 리스트 확장 : extend()
lst1 = [1,2,3]
lst2 = [4,5,6]
print(lst1)
lst1.extend(lst2)
print(lst1)

#3. 요소 중간에 삽입 : insert()
lst1 = [1,2,3,4,5]
lst1.insert(1, 10)
print(lst1)

#4. 요소 제거 : remove()
lst1.remove(10)
print(lst1)

#5. 정렬
lst = [1,5,3,4,6]
lst.sort()
print(lst)
lst.reverse()
print(lst)

# 리스트 길이
print(len(lst))

lst = [100] * 5
print(lst)

lst = [1,2,3,4,5]
print(3 in lst)

lst1 = [10,20,30]
lst2 = [40,50,60]
lst3 = lst1 + lst2 # extend()
print(lst3)

# random
import random
num = random.random()
print(num)

# 1~5 사이 랜덤값
num1 = random.randint(1,5)
print(num1)

lst = [10,20,30,40,50]
num2 = random.choice(lst) # 리스트 값 중 하나를 무작위로 선택
print(num2)

num3 = random.sample(lst,3) # 지정한 배열, 원하는 개수만큼 무작위로 뽑아 리턴
print(num3)

random.shuffle(lst)
print(lst)

