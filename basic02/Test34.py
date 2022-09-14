'''
* Matplotlib *
데이터를 차트나 플롯으로 그려주는 라이브러리 패키지 (시각화)
라인 플롯, 바 차트, 파이차트, box plot, Scatter plot 등
다양한 차트와 스타일 지원.
'''

import matplotlib.pyplot as plt
import numpy as np

# 라인 그래프
# plt.plot([1,2,3,4]) # y축 데이터 지정, x축은 실수값으로 자동 할당
# plt.show() # 그래프 보여주기

# x = range(0, 100)
# y = [v*v for v in x]    # x 값을 반복해서 하나씩 꺼내 각 값의 제곱값을 리스트에 담아서 y에 저장
# print(x)
# print(y)
# plt.plot(x, y)  # x축, y축
# plt.plot(x, y, 'c^') # x, y, style
# plt.show()

# 스타일 변경
# 컬러 : b blue, g green, r red, c cyan, m magenta, y yellow, k black, w while
# 마커 : o circle, v 역삼각형, ^ 삼각형, s 사각형, + 플러스표시, . 점, - 점선

# plt.plot(["Seoul", "Paris", "New York"], [30, 20, 40])
# plt.show()

# 한 화면에 여러 그래프 그리기
# figure 함수를 통해 Figure 객체를 먼저 만들고, add_subplot() 로 그래프 개수만큼 subplot 만들기
# fig = plt.figure()
# gr1 = fig.add_subplot(2, 1, 1) # 2행 1열의 1번째
# gr2 = fig.add_subplot(2, 1, 2) # 2행 1열의 2번째
# plt.show()

# x = range(0, 100)
# y = [v*v for v in x]
# gr1.plot(x, y) # 선 그래프
# gr2.bar(x, y) # 막대 그래프
# plt.show()

# x = np.arange(0.0, 2*np.pi, 0.1)
# sinY = np.sin(x)
# cosY = np.cos(x)
#
# gr1.plot(x, sinY, 'b--')
# gr2.plot(x, cosY, 'r--')

# 각 축에 label 부착
# gr1.set_xlabel('x')
# gr1.set_ylabel('sin(x)')
# gr2.set_xlabel('x')
# gr2.set_ylabel('cos(x)')
#
# # 범례
# gr1.legend(["AAA"], loc='upper right')
# gr2.legend(["BBB"])

# upper right, upper left, lower right/left, right, center right/left,
# lower center, center center, upper cneter

# gr1.text(2,0.5, 'hello')
# gr2.annotate("test", xy=[2, 0.5])

# 그래프 보여주기
# plt.show()

y = [5,9,4,7,2,1]
x = range(len(y))
plt.bar(x, y, width=0.7, color="blue")
plt.show()













