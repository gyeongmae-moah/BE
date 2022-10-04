from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import requests
import re
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["gmmoa"]
col = db["items"]

# mydict = { "col01" : "shane", "col02" : "28 Highway", "col03" : "123-456-789"}

# x = mycol.insert_one(mydict)
# print(x.inserted_id)

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

# for i in range(0, 10, 2):    # 0부터 8까지 2씩 증가

for i in range(len(item)):
    text = no_space(item[i].text)
    i += 1
    print(text)

browser.quit()