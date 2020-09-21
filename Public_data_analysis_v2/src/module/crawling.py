from selenium import webdriver
from bs4 import BeautifulSoup





driver = webdriver.Chrome('Public_data_analysis_v2/src/data/chromedriver')
driver.implicitly_wait(3)
driver.get('http://search.khan.co.kr/search.html?stb=khan&q=%EC%B2%9C%EC%95%88%EB%AC%B8&pg=1&sort=1')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.find_all(class_ = 'd1')
notices