# 네이버 뉴스
import requests
from bs4 import BeautifulSoup

url = "https://n.news.naver.com/mnews/article/011/0004098087?sid=105"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
response = requests.get(url, headers=headers)
print(response)

# HTML 응답 페이지 파싱
soup = BeautifulSoup(response.content, 'lxml')
title = soup.find('title')
print(title)
print(title.text)

# 이미지 찾기
# select() : 값을 여러개, 리스트로 리턴
# select_one() : 값 한개, 리스트에서 풀어서 리턴
img_tag = soup.select_one('#img1') # 값을 리스트에서 풀어서 가져옴
print(img_tag)
print(img_tag['data-src'])

# 이미지 파일 다운 : urllib.request -> urlretrieve() 함수
from urllib.request import urlretrieve # 함수만 하나 임포트
img_url = img_tag['data-src']
file_name = "news_img.jpg"

# 다운 urlretreive(다운받을 데이터의 url, 저장할 파일경로)
urlretrieve(img_url, file_name)

