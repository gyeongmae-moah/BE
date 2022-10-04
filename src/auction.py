# selenium 사용해서 원하는 페이지로 이동 -> 모든 html 크롤링 -> 필요에 따라 정보 추출

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(executable_path='/Users/nagitak/Desktop/gmmoa_back/chromedriver')
browser.get('https://www.courtauction.go.kr/')
browser.switch_to.frame(browser.find_element(By.NAME, 'indexFrame'))


# //*[@id="contents"]/div[4]/form[1]/table/thead/tr/th[7]/a[1]