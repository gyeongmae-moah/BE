from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["gmmoa"]
collection = db["items"]
today = '2022.10.18'
go = True

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

while (go):
    for p in range(2, 10):
        browser.find_element(By.XPATH, f'//*[@id="contents"]/div[4]/form[2]/div/div[1]/a[{p}]/span').click()
        soup = BeautifulSoup(browser.page_source, 'lxml')
        item = soup.find_all('tr', attrs={'class':['Ltbl_list_lvl1', 'Ltbl_list_lvl0']})
        if go == False:
            break
        for i in range(len(item)):
            court = no_space(item[i].find_all('td')[1].text).split()[0]
            name = no_space(item[i].find_all('td')[1].text).split()[1]
            purpose = no_space(item[i].find_all('td')[2].text).split()[1]
            location = no_space(item[i].find_all('td')[3].text).split('[')[0]
            count = -1
            for j in range(len(no_space(item[i].find_all('td')[3].text).split())):
                if no_space(item[i].find_all('td')[3].text).split()[j] == no_space(item[i].find_all('td')[3].text).split()[0]:
                    count += 1
            value = item[i].find_all('td')[5].text.split()[0]
            minimum_cost = item[i].find_all('td')[5].text.split()[1]
            date = item[i].find_all('td')[6].text.split()[1]
            if str(date) != today:
                go = False
                break
            status = no_space(item[i].find_all('td')[6].text).split()[1]

            mydict = { "court": court, "name": name, "purpose": purpose, "location": location, "count": count, "value": value, "minimum_cost": minimum_cost, "date": date, "status": status}
            collection.insert_one(mydict)
browser.quit()