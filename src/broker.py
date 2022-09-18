import requests
import re
from bs4 import BeautifulSoup as bs

# res = requests.get('https://map.naver.com/v5/search/%EA%B2%BD%EB%A7%A4?c=14317597.4804258,4282334.7073563,14.16,0,0,0,dh')
# res.raise_for_status()

# soup = bs(res.text, 'lxml')
# print(soup)

# titles = soup.find_all('span', attrs={'class':'place_bluelink YwYLL'})
# print(titles)

res = requests.get('https://media.naver.com/press/055')
res.raise_for_status()

soup = bs(res.text, 'lxml')
# print(soup)

titles = soup.find_all('span', attrs={'class':'press_news_text'})

for title in titles:
    print(title.strong.text)
