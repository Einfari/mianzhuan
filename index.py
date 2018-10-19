import requests
from bs4 import BeautifulSoup

baseUrl = "http://mianzhuan.wddsnxn.org/"

def getHtmlText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        text = r.content
        soup = BeautifulSoup(text, "html.parser")
        a = soup.find_all('a')
        return a
    except:
        return "Error occurs."

a = getHtmlText(baseUrl)

print(a)