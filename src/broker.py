# import requests
# import re
# from bs4 import BeautifulSoup as bs

# url = 'https://map.naver.com/v5/search/%EA%B2%BD%EB%A7%A4?c=14317597.4804258,4282334.7073563,14.16,0,0,0,dh'
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
# res = requests.get(url, headers=headers)
# res.raise_for_status()

# soup = bs(res.content, 'lxml')
# # print(soup)

# titles = soup.find_all('span', attrs={'class':re.compile('^place_bluelink')})
# print(titles)

# res = requests.get('https://media.naver.com/press/055')
# res.raise_for_status()

# soup = bs(res.content, 'lxml')
# # print(soup)

# titles = soup.find_all('span', attrs={'class':re.compile('press_news_text')})
# # print(titles)

# for title in titles:
#     print(title.strong.text)
