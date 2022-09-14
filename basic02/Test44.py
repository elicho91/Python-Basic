import re

import requests
from bs4 import BeautifulSoup
from pprint import pprint  # 콘솔에 예쁘게 출력하는 라이브러리(자동 줄간격 줄내림 등등)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
html = requests.get("https://comic.naver.com/webtoon/weekday", headers=headers)
soup = BeautifulSoup(html.content, 'lxml')
# print(html)
'''
<div class="list_area daily_all">
    <div class="col" > 요일 하나 * 7
        <div class="inner_col > 
            <h4>월요일</h4>
            <ul>
                <li>웹툰</li>
                <li>웹툰</li>
                <li>웹툰</li>
                <li>웹툰</li>
                <li>웹툰</li>
            </ul>

        </div>
    </div>
</div>

'''

# 1. 월요일 제목들 가져오기
mon = soup.find('div', {'class': 'col_inner'})  # 첫번째 요소 한개만 가져옴 -> 월요일 기둥
# print(mon)
titles = mon.find_all('a', 'title')  # 제목 a태그 전체 가져옴
# pprint(titles)

# 제목만 따로 저장
title_list = []
for t in titles:
    title_list.append(t.text)  # 리스트에 저장
    # print(t.text)

# pprint(title_list)


# 2. 모든 요일 제목들 가져오기
week = soup.find_all('div', class_='col_inner')  # 전체 요일 기둥들
# pprint(week)
# print(len(week))

week_list = []
for day in week:
    # print("-" * 100)
    d_titles = day.find_all('a', 'title')
    title_lists = [t.text for t in d_titles]  # 요일한개의 제목 list
    week_list.append(title_lists)  # 전체 요일 리스트에 요일한개 리스트 추가

# pprint(week_list)
# print(len(week_list))

# 썸네일 이미지 저장
from urllib.request import urlretrieve  # 이미지 저장용
import os, errno  # 폴더 생성, 예외처리용

'''

os.path.isdir   : 이미 디렉토리가 있는지 검사
os.path.join    : 현재 경로를 계산하여 입력한 경로 문자열을 합하여 새로운 경로 만듬
os.makedir      : 지정한 경로로 폴더 생성

'''
try:
    if not (os.path.isdir('image')):  # 현재 위치에 image라는 이름의 폴더가 없으면~
        os.makedirs(os.path.join('image'))  # 만들어라 (경로는 image를 포함한 실제 경로 계산시켜서)
except OSError as e:
    if e.errno == errno.EEXIST:  #
        print("폴더 생성 실패")
        exit()  # 프로그램 강제 종료

# 월요일
img_tag = mon.find_all('img')
# pprint(img_tag)
img_one = img_tag[0]
# print(img_one['title'])
# print(img_one['src'])

for img in img_tag:
    title = img['title']  # 웹툰제목
    title = re.sub('[^0-9a-zA-Zㄱ-힗]', '', title)  # 숫자, 영문대소뭄ㄴ자, 한글을 제외한 나머지 지우가
    img_src = img['src']  # 웹툰 이미지 링크
    print(title, img_src)
    urlretrieve(img_src, 'image/' + title + '.jpg')  # (예시) image/참교육.jpg