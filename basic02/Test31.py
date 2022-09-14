import numpy as np
import numpy as up

# arr = np.arange(10)
# print(arr)
# print(arr[3]) # indexing
# print(arr[2:5]) #  slicing
# arr[2:5] = 15
# print(arr)
# print(arr[3:])
# print(arr[:])

# 다차원
arr2d = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])
print(arr2d)
# 인덱싱
print(arr2d[2,1]) # arr2d[행, 열]
print(arr2d[[2,1],[3,3,]])

# 슬라이싱 [행슬라이싱, 열슬라이싱]
print(arr2d[2, :])
print(arr2d[1:3, :])
print(arr2d[:, 1:3])
print(arr2d[:2, 1:3])
arr2d[:2, 1:3] = 0
print(arr2d)

print("=" * 50)

names = np.array(["AA", "BB", "CC", "DD", "EE"])
print(names)
print(names == "AA")

data = np.random.rand(5,3)
print(data)
print()

print(data[names=="AA", : ]) # 인덱스 번호로 사용
print()
print(data[(names == "AA") | (names == "DD"), :])
print()

print(data)
print(data[:, 1] > 0.5)

data[data[:,1]>0.5 , 1] = 1
print(data)
