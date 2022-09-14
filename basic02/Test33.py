# pandas
# DataFrame
import pandas as pd

sr1 = pd.Series(['a','b','c','d','e'])
print(sr1)
sr2 = pd.Series([1,2,3.14,100,-20])

dic = {'col1':sr1, 'col2':sr2} # dict
df1 = pd.DataFrame(dic)
print(df1)
print(df1.columns)
df1.columns = ["alpha", "nums"]
print(df1)
print(df1.index)
df1.index = ['r0','r1','r2','r3','r4']
print(df1)

# 열 출력
print(df1.alpha)
print(df1["alpha"])
print(df1[["alpha", "nums"]])
print("+" * 100)

# 요소 하나에 접근 [행인덱스, 열이름]
print(df1.loc["r1","nums"])
print(df1.loc["r1":"r3", "alpha":"nums"])










