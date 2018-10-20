import requests
from bs4 import BeautifulSoup

baseUrl = "http://mianzhuan.wddsnxn.org/"

def getHtmlText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Error occurs."


def getContent(url):
    contents = []
    html = getHtmlText(url)

    soup = BeautifulSoup(html, "lxml")
    booklistDom = soup.find("div", class_="booklist")
    booklistContents = booklistDom.contents
    for span in booklistContents:
        content = {}
        linkDom = span.find("a")
        if (linkDom == None):
            continue
        content["title"] = linkDom.text
        content["url"] = linkDom["href"]
        contents.append(content)
    return contents


def save2File(contents):
    with open("./data/mianzhuan.txt", "a+", encoding="utf-8") as f:
        for content in contents:
            f.write("{} \t {} \t \n".format(
                content["title"], content["url"]))


def main(baseUrl):
    contents = getContent(baseUrl)
    save2File(contents)


if (__name__ == "__main__"):
    main(baseUrl)
