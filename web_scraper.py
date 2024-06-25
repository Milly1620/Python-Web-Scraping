import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.vogue.com/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.prettify())

    articles = soup.find_all('h2', class_='article-title')

    titles = [article.get_test() for article in articles]

    df = pd.DataFrame(titles, columns=['Title'])
    df.to_csv('article_titles.csv', index=False)
    
    print('Article titles have been saved to article_titles.csv')
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')