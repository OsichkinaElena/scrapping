import requests
from bs4 import BeautifulSoup


KEYWORDS = {'Chrome', 'C++', 'web', 'python'}
resp = requests.get('https://habr.com/')
soup = BeautifulSoup(resp.text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    text = article.find(class_="article-formatted-body article-formatted-body_version-2") or \
           article.find(class_="article-formatted-body article-formatted-body_version-1")
    text_ = text.text
    text_ = set(text_.split(' '))
    date = article.find('span', class_="tm-article-snippet__datetime-published").text
    header_ = article.find('h2').text
    header = set(header_.split(' '))
    href = article.find('a', class_="tm-article-snippet__title-link").get('href')
    hubs = article.find_all('span', class_="tm-article-snippet__hubs-item")
    hubs = set([hub.text for hub in hubs])
    if KEYWORDS & header or KEYWORDS & hubs or KEYWORDS & text_:
        print(f'{date}----{header_}----{href}')



