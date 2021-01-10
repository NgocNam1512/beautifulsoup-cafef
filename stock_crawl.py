from bs4 import BeautifulSoup
import requests

URLcafef = "https://cafef.vn"
URL = 'https://cafef.vn/timeline/31/trang-1.chn'

for i in range(1, 100):
    URL = 'https://cafef.vn/timeline/31/trang-' + str(i) +'.chn'
    page = requests.get(URL)

    # crawl chúng khoán
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.findAll("a", {"class":"avatar show-popup visit-popup"})

    for result in results:
        print(result.get('href'))
        link = result.get('href')
        URLpage = URLcafef + link
        article = requests.get(URLpage)
        soup2 = BeautifulSoup(article.content, 'html.parser')
        try:
            results2 = soup2.find(id="mainContent")
            all_p = results2.findAll('p')
            main_content = ""
            for p in all_p:
                main_content += p.text
            print(main_content + "\n----------------------------------------")
        except:
            pass

