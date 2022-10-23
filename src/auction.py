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
collection = db["2022-10-24"]
# collection = db["test"]
today = '2022.11.07'

def no_space(text):
    text1 = re.sub('&nbsp; | &nbsp;| \n|\t|\r', '', text)
    text2 = re.sub('\n\n', '', text1)
    return text2

for court in range(1, 61):
    # print('법원 순환')
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
    for page in range(1, 100): # 페이지 순환
        if maintain == False:
            break
        # print('페이지 순환')
        soup = BeautifulSoup(browser.page_source, 'lxml') # html parsing
        item = soup.find_all('tr', attrs={'class':['Ltbl_list_lvl1', 'Ltbl_list_lvl0']}) # 스크래핑 할 element class 지정
        # if no_space(item[0].find_all('td')[1].text).split()[0] == '거창지원':
            # print('거창지원 진입') 
        for i in range(len(item)): # element 순환하며 스크래핑
            court = no_space(item[i].find_all('td')[1].text).split()[0] # 관할 법원
            name = no_space(item[i].find_all('td')[1].text).split()[1] # 사건번호
            purpose = no_space(item[i].find_all('td')[2].text).split()[1] # 목적물
            location = no_space(item[i].find_all('td')[3].text).split('[')[0] # 소재지
            count = -1 
            for j in range(len(no_space(item[i].find_all('td')[3].text).split())): # 하나의 사건번호에 딸린 목적물 개수 (ex. 외 ?건)
                if no_space(item[i].find_all('td')[3].text).split()[j] == no_space(item[i].find_all('td')[3].text).split()[0]:
                    count += 1
            value = item[i].find_all('td')[5].text.split()[0] # 감정평가액
            minimum_cost = item[i].find_all('td')[5].text.split()[1] # 최소매각가격
            date = item[i].find_all('td')[6].text.split()[1] # 매각기일
            if str(date) != today: # 원하는 매각기일이 아닐 경우 중지
                # print('원하는 매각기일 아님')
                maintain = False
                break
            status = no_space(item[i].find_all('td')[6].text).split()[1] # 상태
            # print(f'status:{status}') # '원하는 매각이일 아님 나오고는 나오면 안됨
            if count > 0:
                location = f'{location} 외 {count}건'
            mydict = { "court": court, "name": name, "purpose": purpose, "location": location, "value": value, "minimum_cost": minimum_cost, "status": status}
            collection.insert_one(mydict)

        try:
            if page > 9:
                browser.find_element(By.XPATH, f'//*[@id="contents"]/div[4]/form[2]/div/div[1]/a[11]').click() # 화살표 클릭
            else:
                browser.find_element(By.XPATH, f'//*[@id="contents"]/div[4]/form[2]/div/div[1]/a[{page}]').click() # 다음 페이지 클릭
        except:
            maintain = False
            break
browser.quit()



    # while (maintain):
    #     print('페이지 순환 윗라인')
    #     for page in range(1, 100): # 페이지 순환
    #         if maintain == False:
    #             break
    #         print('페이지 순환')
    #         soup = BeautifulSoup(browser.page_source, 'lxml') # html parsing
    #         item = soup.find_all('tr', attrs={'class':['Ltbl_list_lvl1', 'Ltbl_list_lvl0']}) # 스크래핑 할 element class 지정
    #         # if no_space(item[0].find_all('td')[1].text).split()[0] == '거창지원':
    #             # print('거창지원 진입') 
    #         for i in range(len(item)): # element 순환하며 스크래핑
    #             court = no_space(item[i].find_all('td')[1].text).split()[0] # 관할 법원
    #             name = no_space(item[i].find_all('td')[1].text).split()[1] # 사건번호
    #             purpose = no_space(item[i].find_all('td')[2].text).split()[1] # 목적물
    #             location = no_space(item[i].find_all('td')[3].text).split('[')[0] # 소재지
    #             count = -1 
    #             for j in range(len(no_space(item[i].find_all('td')[3].text).split())): # 하나의 사건번호에 딸린 목적물 개수 (ex. 외 ?건)
    #                 if no_space(item[i].find_all('td')[3].text).split()[j] == no_space(item[i].find_all('td')[3].text).split()[0]:
    #                     count += 1
    #             value = item[i].find_all('td')[5].text.split()[0] # 감정평가액
    #             minimum_cost = item[i].find_all('td')[5].text.split()[1] # 최소매각가격
    #             date = item[i].find_all('td')[6].text.split()[1] # 매각기일
    #             if str(date) != today: # 원하는 매각기일이 아닐 경우 중지
    #                 print('원하는 매각기일 아님')
    #                 maintain = False
    #                 break
    #             status = no_space(item[i].find_all('td')[6].text).split()[1] # 상태
    #             if count > 0:
    #                 location = f'{location} 외 {count}건'
    #             mydict = { "court": court, "name": name, "purpose": purpose, "location": location, "value": value, "minimum_cost": minimum_cost, "status": status}
    #             collection.insert_one(mydict)

    #         try:
    #             if page > 10:
    #                 browser.find_element(By.XPATH, f'//*[@id="contents"]/div[4]/form[2]/div/div[1]/a[11]').click() # 화살표 클릭
    #             else:
    #                 browser.find_element(By.XPATH, f'//*[@id="contents"]/div[4]/form[2]/div/div[1]/a[{page}]').click() # 다음 페이지 클릭
    #         except:
    #             maintain = False
    #             break
