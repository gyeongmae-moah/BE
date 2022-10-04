# selenium 사용해서 원하는 페이지로 이동 -> 모든 html 크롤링 -> 필요에 따라 정보 추출

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import requests
import re

def no_space(text):
    text1 = re.sub('&nbsp; | &nbsp;| \n|\t|\r', '', text)
    text2 = re.sub('\n\n', '', text1)
    return text2

browser = webdriver.Chrome(executable_path='/Users/nagitak/Desktop/gmmoa_back/chromedriver')
browser.get('https://www.courtauction.go.kr/')
browser.switch_to.frame(browser.find_element(By.NAME, 'indexFrame'))
browser.find_element(By.ID, 'main_btn').click()
browser.find_element(By.XPATH, '//*[@id="contents"]/div[4]/form[1]/table/thead/tr/th[7]/a[1]').click()
browser.find_element(By.XPATH, '//*[@id="contents"]/div[4]/form[1]/table/thead/tr/th[7]/a[1]').click()

soup = BeautifulSoup(browser.page_source, 'lxml')

item = soup.find_all('td')

for i in range(len(item)):
    text = no_space(item[i].text)
    print(text)


# movies = soup.find_all('div', attrs={'class':['class1', 'class2']})
# //*[@id="contents"]/div[4]/form[1]/table/thead/tr/th[7]/a[1]
# items = soup.find_all('li', attrs={'text':re.compile('^abc')})
# soup.find('td', text=re.compile('$서울중앙지방법원')
# p = re.compile('ca.e')
# soup.find_next_siblings('td', attrs={'class':'Ltbl_list_lvl0'})
# var1 = soup.find('tbody')
# print('result:', var1.td.input['value'].split(',')[0])
# rank1.find_next_sibling('li') # 개행 무시하고 그 다음의 li element 출력
# s = 'hello-world-123-good-984'
# m = re.findall('[a-zA-Z]+',s)
# print(m) // 출력결과 ['hello', 'world', 'good']
# re.findall('[ㄱ-힣]+', elem[10].text)