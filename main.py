from bs4 import BeautifulSoup
import requests

URL = 'https://cafef.vn/'
page = requests.get(URL)

crawl góc nhà đầu tư
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.findAll("a", {"class": "bndt-item-title"})
for result in results:
    print(result.get('title'))

# crawl full tin
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.findAll("div", {"class": "knswli-right"})
for result in results:
    title = result.find('h3')
    title = title.find('a')
    print(title.get('title'))
    print("-----")