# pandas
import pandas as pd
data1 = ['a', 'b', 'c', 'd', 'e']
print(data1)
print(type(data1))
print("=" * 50)
# 1차원 Series 생성
sr1 = pd.Series(data1)
print(sr1)
print("=" * 50)

sr2 = pd.Series(data=[11,22,33,44], index=['a','b','c','d'])
print(sr2)
print("=" * 50)

# 인덱싱
print(sr2['a'])
print(sr2[2:4])
#[[]] 안에 인ㄴ덱스값을 넣어주면 행에 접근 가능
print(sr2[['a','c']]) # a,c 인덱스 두개 가져오기
# 슬라이싱
print(sr2['a':'c']) # a,c 인덱스 슬라이싱
print(sr2.index) # index만 가져오기
print(sr2.dtype)
print(sr2.values)
print("=" * 50)

#연산
print(sr2)
print(sr2 * 2)
print("=" * 50)

sr3 = pd.Series(data=[11,22,33,44], index=['a','b','d','e'])
print(sr2)
print(sr3)

print(sr2 + sr3)

print(sr2.sum())    # 합계
print(sr2.mean())   # 평균
print(sr2.median()) # 중간값
print(sr2.max()) # 최댓값
print(sr2.sort_values)
print(sr2.sort_index)

print("=" * 50)

print(sr2.loc["a"])
print(sr2.loc['a' : 'c'])

