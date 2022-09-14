'''
# Word Cloud
    tag cloud 또는 word cloud는
    메타데이터에서 얻어진 태그들을 분석하여
    중요도나 인기도 등을 고려하여 시각적으로 늘어놓아 표시하는 것
    보통은 2차원의 표와 같은 형태로 태그들이 배치되며, 이때 순서는 알파벳/가나다 순으로 배치된다.
    시각적인 중요도를 강조하기 위해 각 태그들은 그 중요도/인기도에 따라
    글자의 색상이나 굵기 등 형태가 변한다.

# KoNLPy
    한글 자연어 처리에 맞춤화된 파이썬 오픈 소슷 라이브러리
    https://konlpy.org/ko/v0.6.
    # 형태 분석기 클래스
        5가지 클래스 포함.
            - Hannaum
            - Kkma
            - Komoran
            - Mecab
            - Okt (구, Twitter)

# 라이브러리 설치
    wordcloud : 시각화
    konlpy : 한글 자연어 처리
'''

from wordcloud import WordCloud
from konlpy.tag import Okt

#2. Okt 객체 생성
okt = Okt()

# 함수들
# morphs(문자) : 형태소 단위로 구분 분석해 수행함
# print(okt.morphs("안녕하세요, 제이름은 피카츄입니다."))
# # nouns(문자) : 명사만 추출
# print(okt.nouns("안녕하세요, 제이름은 피카츄입니다."))
# print(okt.nouns("사과오이수박복숭아"))
# print(okt.nouns("띄어쓰기안했는데명사를추출할수있겠니"))
#phrases(문장) : 어절만 추출
# print(okt.phrases("오늘은 날씨가 참 좋네요"))
# pas(문장, norm=False, stem=False) : 형태로 단위로 쪼갠후 각 품사들을 태깅해서 리스트로 리턴
# print(okt.pos("이렇게 똑똑한 module이 있다니!! 완전 신기함 ㅋㅋㅋㅋ : ", norm=True))

# 한글 명사 빈도
from collections import Counter

# 네이버 뉴스
news = ""
with open("new_sample.txt", 'r', encoding='utf-8') as file:
    news = file.read()

print(news)

# 명사 추출
noun = okt.nouns(news)
print(noun) # 리스트로 리턴
print(len(noun)) # 전체 개수


counter = Counter(noun) # 카운터 객체 생성하며 list 주면
print(counter)
# 명사 빈도수 카운트
noun_list = counter.most_common(10) # 빈도수 높은순으로 n순위까지 리스트로 리턴
print(noun_list)

# 것, 의, 등 한글자 명사 뺴기
for i, v in enumerate(noun):
    if len(v) < 2:
        noun.pop(i)

counter = Counter(noun)
noun_list = counter.most_common(100) # 빈도수 높은순으로 n순위까지 리스트로 리턴
print(noun_list)

# 추출된 결과를 txt 파일로 저장
with open("noun_list.txt", 'w', encoding='utf-8') as f:
    for v in noun_list:
        f.write(str(v))
        f.write("\n")

# csv 파일로 저장 comma sepreated value
# import csv
# with open('noun_list.csv', 'w', encoding='utf-8') as f:
#     csvw = csv.writer(f)
#     for v in noun_list:
#         csvw.writerow(v)

# 워드 클라우드
wc = WordCloud(font_path='C:\\Windows\\Fonts\\gulim.ttc', background_color='white',max_words=100)
wc.generate(news)
wc.to_file('wordcloud_news.png')

# 빈도수 순으로 추출한 명사 리스트
wc.generate_from_frequencies(dict(noun_list))
wc.to_file('worldcloud')
























