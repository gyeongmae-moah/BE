from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re
import pymongo

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["gmmoa"]
collection = db["2022-10-14"]
today = '2022.10.28'

def no_space(text):
    text1 = re.sub('&nbsp; | &nbsp;| \n|\t|\r', '', text)
    text2 = re.sub('\n\n', '', text1)
    return text2

for court in range(1, 61):
    maintain = True
    browser = webdriver.Chrome(executable_path='/Users/nagitak/Desktop/gmmoa_back/chromedriver', chrome_options=options)
    browser.get('https://www.courtauction.go.kr/')
    browser.switch_to.frame(browser.find_element(By.NAME, 'indexFrame')) # 사용 프레임 변경
    browser.find_element(By.XPATH, f'//*[@id="idJiwonNm1"]/option[{court}]').click() # 법원 순환
    browser.find_element(By.ID, 'main_btn').click() # 검색
    try:
        browser.find_element(By.XPATH, '//*[@id="contents"]/div[4]/form[1]/table/thead/tr/th[7]/a[1]').click() # 매각기일 내림차순 정렬
        browser.find_element(By.XPATH, '//*[@id="contents"]/div[4]/form[1]/table/thead/tr/th[7]/a[1]').click()
    except:
        continue
    while (maintain):
        for page in range(1, 10):
            soup = BeautifulSoup(browser.page_source, 'lxml') # html parsing
            item = soup.find_all('tr', attrs={'class':['Ltbl_list_lvl1', 'Ltbl_list_lvl0']}) # 스크래핑 할 element 지정
            if maintain == False:
                break
            for i in range(len(item)):
                court = no_space(item[i].find_all('td')[1].text).split()[0] # 관할 법원
                name = no_space(item[i].find_all('td')[1].text).split()[1] # 사건번호
                purpose = no_space(item[i].find_all('td')[2].text).split()[1] # 목적물
                location = no_space(item[i].find_all('td')[3].text).split('[')[0] # 소재지
                count = -1 # 하나의 사건번호에 목적물 개수 (ex. 외 ?건)
                for j in range(len(no_space(item[i].find_all('td')[3].text).split())):
                    if no_space(item[i].find_all('td')[3].text).split()[j] == no_space(item[i].find_all('td')[3].text).split()[0]:
                        count += 1
                value = item[i].find_all('td')[5].text.split()[0] # 감정평가액
                minimum_cost = item[i].find_all('td')[5].text.split()[1] # 최소매각가격
                date = item[i].find_all('td')[6].text.split()[1] # 매각기일
                if str(date) != today: # 원하는 매각기일이 아닐 경우 중지
                    maintain = False
                    break
                status = no_space(item[i].find_all('td')[6].text).split()[1] # 상태
                if count > 0:
                    location = f'{location} 외 {count}건'
                mydict = { "court": court, "name": name, "purpose": purpose, "location": location, "value": value, "minimum_cost": minimum_cost, "status": status}
                collection.insert_one(mydict)

            try:
                browser.find_element(By.XPATH, f'//*[@id="contents"]/div[4]/form[2]/div/div[1]/a[{page}]/span').click() # 페이지 순환
            except:
                maintain = False
                break
browser.quit()

