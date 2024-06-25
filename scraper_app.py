
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://fentybeauty.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())

titles = []
urls = []
summaries = []

#extraction for titles
for title_tag in soup.find_all('h2', class_='aticle-title'):
    titles.append(title_tag.text.strip())


#extraction for titles
for link_tag in soup.find_all('a', class_='article-link'):
    urls.append(link_tag.get('href'))

#extraction for summaries
for paragraph_tag in soup.find_all('p', class_='article-summary'):
    summaries.append(paragraph_tag.text.strip())

data = list(zip(titles, urls, summaries))

with open ('article_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'URL', 'Summary'])
    writer.writerows(data)

print("Data successfully written to article_data.csv")




