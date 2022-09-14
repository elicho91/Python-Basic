'''
* numpy *
- 수치 데이터를 다루는 패키지
    다차원 행렬 자료구조인 ndarray를 통해 벡터 및 행렬을 사용하는 선형 대수 계산에 주로 사용
    속도가 빠름
    .array()
    .asarray()
    .arange()
    .linspace(start,end,num)
    .logspace(start,end,num)

* pandas *
- 파이썬 데이터 처리를 위한 라이브러리
    데이터 분석같은 작업에서 거의 필수로 사용, 행과 열을 이루어진 데이터 객체를 만들어
    보다 안정적으로 대용량 데이터를 처리하는데 편리하며, 속도가 빠름
    1차원 배열 형태의 Series 자료구조와 2차원 배열 형태의 DataFrame 자료구조를 지원

1) 라이브러리 추가
    numpy   : 
    pandas  : 
    
    (matplotlib : 그래프)
    (scikit-lean : 머신러닝 - 선형회귀)
'''

import numpy as np
#1. 리스트 1차원 배열 생성
data1 = [3,
         6,
         5,
         7,
         4,
         9]
arr1 = np.array(data1)
print(arr1)
print(arr1.shape) # 배열 구조 출력:(6,) (행,열)

#2. 리스트로 2차원 배열 생성
data2 = [
    [1,2,3,4],
    [5,6,7,8]
]
print(data2)
arr2 = np.array(data2)
print(arr2)
print(arr2.shape)
print(arr2.ndim)
print(arr2.size)

#3. 숫자로 채워진 배열 생성
print(np.arange(15))
print(np.arange(1, 10, 2)) # (start,end-1,stop)

#4. zero 배열 생성 (행,열)
print(np.zeros((3,3)))

#5. 1 배열 생성
print(np.ones((2,3)))

#6. 특정 값으로
print(np.full((2,2),7))

#7. 대각선으로 1채우고 나머지 0인 배열
print(np.eye(3))

#8. 랜덤값 채운 배열
print(np.random.random(4))
print(np.random.rand(2,2))

#9. 다차원 배열로 변형
print(arr1.reshape(2,3))
print(arr1.dtype)
#int : int34, int64, float34, float64

# 11. 형변환 astype()
arr3 = arr1.astype(np.float64)
print(arr1)
print(arr3)

arr4 = np.array([[1,2,3,],[4,5,6]])
print(arr4)
arr5 = np.array([[11,22,33],[44,55,66]])
print(arr5)

print(arr4 + arr5)
print(arr4 - arr5)
print(arr4 * arr5)
print(arr4 / arr5)




















