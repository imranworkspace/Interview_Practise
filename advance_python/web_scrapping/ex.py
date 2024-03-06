import requests
import bs4

res = requests.get("https://en.wikipedia.org/wiki/Machine_learning")
print(type(res))

soup=bs4.BeautifulSoup(res.text,"html5lib")
print(soup)

soup.select(".mw-headline")
for i in soup:
    print(i,end='')