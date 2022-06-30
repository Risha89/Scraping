import requests
import bs4
base_url = 'https://habr.com/ru/all/'
KEYWORDS = ['дизайн', 'фото', 'web', 'python']
response = requests.get(base_url, headers='')
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    previews = article.find_all(class_='tm-article-snippet')
    previews = [preview.text.strip() for preview in previews]
    for preview in previews:
        for word in KEYWORDS:
            if word in preview:
                time = article.find(class_='tm-article-snippet__datetime-published').text
                href = article.find(class_='tm-article-snippet__title-link').attrs['href']
                title = article.find('h2').find('span').text
                print(time, title, base_url + href )
