from bs4 import BeautifulSoup
html = """
<html>
    <head>
        <title class="a" id="tid">test title</title>
    </head>
    <body>
        <p>HAHAHAHA</p>
        <p class = "a" id='a'>HAHAHAHA</p>
        <p class = 'b'> HAHAHAHA </p>
    </body>
</html>
"""
soup = BeautifulSoup(html, 'lxml')

# 원하는 요소 정확히 접근하기  #자주 쓸거임!!
# find_all()
print(soup.find_all('title'))  # [<title class="t" id="tid">test title</title>]
print(soup.find_all('p')) # [<p>HAHAHAHA</p>, <p>HAHAHAHA</p>, <p>HAHAHAHA</p>]
print(soup.find_all(id= 'a')) # [<p id="a">HAHAHAHA</p>]
print(soup.find_all(id=True))  # [<p id="a">HAHAHAHA</p>]
                                # 아이디 속성을 가지고 있는거 모두

print(soup.find_all(id=False)) # 속성이 없는거
print(soup.find_all('p', id='a')) # p태그이면서 속성이 a인것

print(soup.find_all(class_='a'))  # 클래스가 a인것
print(soup.find_all('p', class_='a'))
print(soup.find_all('p', limit=2)) # 앞에 두개만 가져옴

# 리스트 형태로 태그명 여러개 검색
print(soup.find_all(['title', 'p']))

# 응용 : 두번 거르기
body_tag = soup.find_all('body')
print(body_tag)
print(body_tag[0].find_all('p'))

# find() : 하나의 요소만 가져옴 -> 문서상에 요소가 하나만 존재할 경우 사용하는 것이 좋다.
print(soup.find('p'))

# select() : CSS 셀럭터를 이용하여 원하는 요소 리스트로 리턴받기
html = """
<html>
    <head>
        <title class="a">test title</title>
    </head>
    <body>
        <p class="a">HAHAHAHA1111</p>
        <p class = "b" id=p'\>HAHAHAHA22222</p>
        <p class = "b"> HAHAHAHA33333 </p>
        <a href="/example/test01">a tag</a>
        <b>b tag</b>
    </body>
</html>
"""
soup = BeautifulSoup(html, 'lxml')
print(soup.select('p')) # 태그명
print(soup.select('a'))
print(soup.select('.b'))
print(soup.select('#p'))
print(soup.select('p#p')) # 태그명#id값 태그명.클래스값

print(soup.select('body .a'))
# extract() : 태그 제거
print("*"*100)
p_tag = soup.select('p')
print(p_tag)
for p in p_tag:
    print(p.extract())
print(soup)