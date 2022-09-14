'''
동적 페이지 크롤링
* selenium *
브라우저를 제어해서 크롤링 하는 방법
Selenium 은 주로 웹앱을 테스트하는데 이용한 프레임워크다.
webdriver라는 API를 통해 운영체제에 설치된 Chrome등의 브라우저를
가상 브라우저로 제어하게 된다.

라이브러리 설치
    selenium 모듈 설치 : python interpreter > selenium 검색+설치
    (구)chromedriver 다운 : 현재 본인 PC에서 사용중인 크롬 브라우저의 버전을 확인
                     https://chromedriver.chromium.org/downloads
                    브라우저 버전과 운영체제에 맞는 드라이버 다운

        * 브라우저 띄우고 아래와 같은 에러 메세지 발생시, 신 버전으로 실행 *
        DeprecationWarning: executable_path has been deprecated,
        please pass in a Service object
            driver = webdriver.Chrome('chromedriver.exe')

    (신) webdriver-manager 모듈 설치

    * (신)selenium으로 브라우저 DOM에 접근하는 함수들  *
    find_element(By.상수, '선택자 또는 값')  : 요소 한개 찾기
    find_elements(By.상수, '선택자 또는 값') : 요소 여러개 찾기

    By.ID
    By.NAME
    By.XPATH
    By.TAG_NAME
    By.CLASS_NAME
    By.CSS_SELECTOR

    xpath : XML Path Language
    W3C 표준으로 XML 문서의 구조를 통해 경로(path)위에, 지정한 구문을 사용하여
    항목을 배치하고 처리하는 언어.
    /       : 절대경로
    //          : 문서내에서 검색
    //@href : href 속성이 있는 모든 태그
    //a[@href="http://google.com"]  : a태그의 href 속성이 해당 주소값을 가진 모든 태그
    (//a)[3] : 문서의 세번째 a 태그
    //table/tr/*    : 모든 테이블태그에서 모든 자식 tr태그안 모든것
    //div[@*]       : 속성이 하나라도 있는 div 태그
    //div[@id="hello"]

    * (구)selenium으로 브라우저 DOM에 접근하는 함수들  *
    find_element_by_id('id값')
    find_element_by_tag_name('태그명')
    find_element_by_class_name
    find_element_by_css_selector
    find_element_by_xpath
    find_elements_by_tag_name
    find_elements_by_class_name
    find_elements_by_css_selector
    find_elements_by_xpath
    ....

'''
import time

from selenium import webdriver
# (구)브라우저 띄우기
# driver = webdriver.Chrome('chromedriver.exe')

# (신) 브라우저 띄우기
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # selenium 으로 DOM문서 검색시, 검색수단을 지정하는 상수 모듈
from selenium.webdriver import Keys, ActionChains
from webdriver_manager.chrome import ChromeDriverManager
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True) # 브라우저 창 안 닫히게 하는 옵션
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)

# 네이버 띄우기
# url = "http://www.naver.com"
# driver.get(url)
# input_tag = driver.find_element(By.CSS_SELECTOR, 'input#query')
# input_tag.send_keys('파이썬')
# 검색 버튼 찾아서 버튼 클릭!
# search_btn = driver.find_element(By.ID, 'search_btn')
# search_btn.click()
# 입력란에 작성후 엔터 키 누르기
# input_tag.send_keys(Keys.ENTER)

# 구글 지도 검색
url = "https://www.google.co.kr/maps"
driver.get(url)
time.sleep(5)

input_tag = driver.find_element(By.ID, 'searchboxinput')
input_tag.send_keys('신촌역 맛집')
input_tag.send_keys(Keys.ENTER)
time.sleep(5)

list_div = driver.find_elements(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div')
print(len(list_div))
action = ActionChains(driver)
action.move_to_element(list_div[15]).perform()
time.sleep(5)
list_div = driver.find_elements(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div')
print(len(list_div))
action.move_to_element(list_div[29]).perform()
time.sleep(5)
list_div = driver.find_elements(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div')
print(len(list_div))

'''
//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[3]
//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[5]
//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[7]

'''

for i in range(3, 42, 2):
    xpath = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div['+ str(i) +']/div/a'

    search_item = driver.find_element(By.XPATH, xpath)
    search_item.click()
    time.sleep(5)

    try:
        addr = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[3]/button/div[1]/div[2]/div[1]')
        print(addr.text)
    except Exception as e:
        print("exception!!", e)
        pass
    try:
        website = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[5]/a/div[1]/div[2]/div[1]')
        print(website.text)
    except Exception as e:
        print("exception!!", e)
        pass

    driver.back() # 브라우저 뒤로가기
# 검색 목록

'''
* selector
#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd > div:nth-child(1) > div > a
#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd > div:nth-child(3) > div > a
#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd > div:nth-child(5) > div > a
* xpath
//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[1]/div/a
//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/a
//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[5]/div/a

//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[3]/button/div[1]/div[2]/div[1]
'''




















