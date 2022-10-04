# selenium 사용해서 원하는 페이지로 이동 -> 모든 html 크롤링 -> 필요에 따라 정보 추출

from selenium import webdriver

browser = webdriver.Chrome(executable_path='/Users/nagitak/Desktop/gmmoa_back/chromedriver')
browser.get('https://www.courtauction.go.kr/')