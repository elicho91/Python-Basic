'''
카톡 워드 클라우드
'''

from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter

chat = ''
with open('KakaoTalk__group.txt','r',encoding='utf-8')as txt:
    lines = txt.readlines()
    for l in lines:
        #print(l[l.rfind(']') +1 :])
        chat += l[l.rfind(']')+1 :]
#print(type(chat)) #<class 'list'>

#print(chat)

import re

chatRe = re.sub('[-=+,#@/\?:^$.*\"!~&%\\|\)\(\[\]\<\>`\']', '', chat)
chatRe = re.sub('[0-9]','',chatRe)
chatRe = re.sub('[A-Za-z]','',chatRe)
chatRe = re.sub('이모티콘','',chatRe)
chatRe = re.sub('사진','',chatRe)
chatRe = re.sub('년 월 일','',chatRe)
chatRe = chatRe.replace("ㅋ", '')

#명사만 추출
okt = Okt()
noun = okt.nouns(chatRe)


#한글자 명사 삭제
for i,v in enumerate(noun):
    if len(v) <2:
        noun.pop(i)

#명사 빈도 카운트
count = Counter(noun)
noun_list= count.most_common(100)
print(noun_list)

#원드 클라우드로 띄우기
wc = WordCloud(font_path='C:\\Users\\tjoeun\\AppData\\Local\\Microsoft\\Windows\\Fonts\\D2Coding-Ver1.3.2-20180524-all.ttc', background_color='white', max_words=100,height=1000,colormap='PiYG',width=500)
wc.generate(chatRe)
wc.to_file('kakado.png')

#마스크 씌우기
from PIL import Image
import numpy as np
import  matplotlib.pyplot as plt

mask = Image.open('cloud.png')
mask = np.array(mask)

wc = WordCloud(font_path='C:\\Users\\tjoeun\\AppData\\Local\\Microsoft\\Windows\\Fonts\\D2Coding-Ver1.3.2-20180524-all.ttc', background_color='white', max_words=100,height=1000,colormap='PiYG',width=500,mask=mask)
wc.generate_from_frequencies(dict(noun_list))
wc.to_file('kakao2.png')

#화면에 띄우기
plt.figure()
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()