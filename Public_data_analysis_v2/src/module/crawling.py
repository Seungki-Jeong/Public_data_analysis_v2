from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import re

# 경향신문 크롤링
def kh():
    # 경향신문 '천안문 검색 결과' URL
    url = 'http://search.khan.co.kr/search.html?stb=khan&q=%EC%B2%9C%EC%95%88%EB%AC%B8&pg={}&sort=1'

    # 가져올 텍스트 공간 초기화
    global kh_word
    kh_word = []

    # 경향신문 1~10페이지까지 크롤링 (최대 10페이지까지 존재)
    for count in tqdm(range(1, 11)):

    #     1~10페이지까지 html을 가져옴
        response = requests.get(url.format(count))
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

    #     title 부분
        titles = soup.select('.phArtc > dt > a')
    #     소제목 부분
        words = soup.select('.phArtc > .txt')

    #     타이틀과 소제목을 모두 합침
        for tit, wor in zip(titles, words):
            kh_word.append(tit.text)
            kh_word.append(wor.text)

#     크롤링한 텍스트 데이터 저장
    with open('D:/workspace/Public_data_analysis_v2/Public_data_analysis_v2/src/data/kh.txt', mode = 'wt', encoding = 'utf-8') as file:
        for w in kh_word:

            # 정규식 전처리
            w = re.sub(r'[-\'@#:/a-zA-Z<>!-"·‘*\(\)]', '', w)
            w = re.sub(r'[ ]+', ' ', w)
            #             "" 제거
            w = re.sub(r'[“”]', ' ', w)
            #             특수문자 제거
            w = re.sub(r'[^\w\s]', '', w)
            #             []안 문자 제거
            w = re.sub(r'\[.*?\]', '', w)

            # 한 줄씩 저장
            file.writelines('{}\n'.format(w))


def kh_open():
    with open('D:/workspace/Public_data_analysis_v2/Public_data_analysis_v2/src/data/kh.txt', mode='r',encoding='utf-8') as file:
        global kh_text
        kh_text = file.readlines()
        for i, w in enumerate(kh_text):
            kh_text[i] = w.replace('\n', '')


# 동아일보 크롤링
def donga():
    # 동아일보 '천안문 검색 결과' URL
    url = 'https://www.donga.com/news/search?p={}&query=%EC%B2%9C%EC%95%88%EB%AC%B8&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1'

    # 가져올 텍스트 공간 초기화
    global donga_word
    donga_word = []

    # 동아일보 1~1051페이지까지 크롤링 (최대 10페이지까지 존재)
    for count in tqdm(range(1, 1052)):
    #     1~1051페이지까지 html을 가져옴
        response = requests.get(url.format(count))
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

    #     title 부분
        titles = soup.select('.searchList > .t > .tit > a')
    #     소제목 부분
        words = soup.select('.searchList > .t > .txt > a')

    #     타이틀과 소제목을 모두 합침
        for tit, wor in zip(titles, words):
            donga_word.append(tit.text)
            donga_word.append(wor.text)

    #     크롤링한 텍스트 데이터 저장
    with open('D:/workspace/Public_data_analysis_v2/Public_data_analysis_v2/src/data/donga.txt', mode = 'wt', encoding = 'utf-8') as file:
        for w in donga_word:

            # 정규식 전처리
            w = re.sub(r'[-\'@#:/a-zA-Z<>!-"·‘*\(\)]', '', w)
            w = re.sub(r'[ ]+', ' ', w)
            #             "" 제거
            w = re.sub(r'[“”]', ' ', w)
            #             특수문자 제거
            w = re.sub(r'[^\w\s]', '', w)
            #             []안 문자 제거
            w = re.sub(r'\[.*?\]', '', w)

            file.writelines('{}\n'.format(w))

def donga_open():
    with open('D:/workspace/Public_data_analysis_v2/Public_data_analysis_v2/src/data/donga.txt', mode='r',encoding='utf-8') as file:
        global donga_text
        donga_text = file.readlines()
        for i, w in enumerate(donga_text):
            donga_text[i] = w.replace('\n', '')


# 한겨레 크롤링
def hani():
    # 한겨레 '천안문 검색 결과' URL
    url = 'http://search.hani.co.kr/Search?command=query&keyword=%EC%B2%9C%EC%95%88%EB%AC%B8&media=news&submedia=&sort=d&period=all&datefrom=1988.01.01&dateto=2020.09.22&pageseq={}'

    # 가져올 텍스트 공간 초기화
    global hani_word
    hani_word = []

    # 동아일보 1~1051페이지까지 크롤링 (최대 10페이지까지 존재)
    for count in tqdm(range(0, 78)):
    #     1~1051페이지까지 html을 가져옴
        response = requests.get(url.format(count))
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

    #     title 부분
        titles = soup.select('.search-result-list > li > dl > dt > a')
    #     소제목 부분
        words = soup.select('.search-result-list > li > dl > .detail')

    #     타이틀과 소제목을 모두 합침
        for tit, wor in zip(titles, words):
            hani_word.append(tit.text)
            hani_word.append(wor.text)

    #     크롤링한 텍스트 데이터 저장
    with open('D:/workspace/Public_data_analysis_v2/Public_data_analysis_v2/src/data/hani.txt', mode = 'wt', encoding = 'utf-8') as file:
        for w in hani_word:

            # 정규식 전처리
            w = re.sub(r'[-\'@#:/a-zA-Z<>!-"·‘*\(\)]', '', w)
            w = re.sub(r'[ ]+', ' ', w)
            #             "" 제거
            w = re.sub(r'[“”]', ' ', w)
            #             특수문자 제거
            w = re.sub(r'[^\w\s]', '', w)
            #             []안 문자 제거
            w = re.sub(r'\[.*?\]', '', w)

            file.writelines('{}\n'.format(w))

def hani_open():
    with open('D:/workspace/Public_data_analysis_v2/Public_data_analysis_v2/src/data/hani.txt', mode='r',encoding='utf-8') as file:
        global hani_text
        hani_text = file.readlines()
        for i, w in enumerate(hani_text):
            hani_text[i] = w.replace('\n', '')


# 조선일보 크롤링
def chosun():
    
#     가져올 텍스트 공간 초기화
    global chosun_word
    chosun_word = []

#     selenium로 웹페이지 제어하고 ULR 접속
    driver = webdriver.Chrome('../data/chromedriver')
    driver.implicitly_wait(3)
    driver.get('https://www.chosun.com/search/query=%EC%B2%9C%EC%95%88%EB%AC%B8/')

#     웹페이지에서 더보기 페이지 전부 펴기
    while True:
        try:
            driver.find_element_by_id('load-more-stories').click()
        except:
            break

#     BeautifulSoup 크롤링을 위해 page_sorce 가져오기
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

#     title 부분
    titles = soup.select('.story-card-wrapper > .story-card > .story-card-right > .story-card__headline-container > h3 > a > span')
#     소제목 부분
    words = soup.select('.story-card-wrapper > .story-card > .story-card-right > .story-card__deck > span')

#      타이틀과 소제목을 합침
    for tit, wor in zip(titles, words):
            chosun_word.append(tit.text)
            chosun_word.append(wor.text)

    #     크롤링한 텍스트 데이터 저장
    with open('D:/workspace/Public_data_analysis_v2/Public_data_analysis_v2/src/data/chosun.txt', mode = 'wt', encoding = 'utf-8') as file:
        for w in chosun_word:

            # 정규식 전처리
            w = re.sub(r'[-\'@#:/a-zA-Z<>!-"·‘*\(\)]', '', w)
            w = re.sub(r'[ ]+', ' ', w)
            #             "" 제거
            w = re.sub(r'[“”]', ' ', w)
            #             특수문자 제거
            w = re.sub(r'[^\w\s]', '', w)
            #             []안 문자 제거
            w = re.sub(r'\[.*?\]', '', w)

            file.writelines('{}\n'.format(w))

def chosun_open():
    with open('D:/workspace/Public_data_analysis_v2/Public_data_analysis_v2/src/data/chosun.txt', mode='r',encoding='utf-8') as file:
        global chosun_text
        chosun_text = file.readlines()
        for i, w in enumerate(chosun_text):
            chosun_text[i] = w.replace('\n', '')
