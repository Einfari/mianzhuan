import requests
from bs4 import BeautifulSoup
import os

baseUrl = "http://mianzhuan.wddsnxn.org/"


def getHtmlText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Error occurs."


def getContents(url):
    contents = []
    html = getHtmlText(url)

    soup = BeautifulSoup(html, "lxml")
    booklistDom = soup.find("div", class_="booklist")
    booklistContents = booklistDom.contents
    for span in booklistContents:
        content = {}
        linkDom = span.find("a")
        if linkDom == None:
            continue
        content["title"] = linkDom.text
        content["url"] = linkDom["href"]
        contents.append(content)
    return contents


def getChapterContent(url):
    perHtml = getHtmlText(url).replace("<br/>", "\n")
    perSoup = BeautifulSoup(perHtml, "lxml")
    chapterDom = perSoup.find("div", class_="bookcontent")
    if chapterDom == None:
        return None
    return chapterDom.text


def savePerChapter2File(contents):
    distFolder = "./data/mianzhuan/"
    if not os.path.exists(distFolder):
        os.mkdir(distFolder)
    count = 1
    for content in contents:
        title = content["title"]
        url = content["url"]
        dist = distFolder + str(count) + "-" + title + ".txt"
        if not os.path.exists(dist):
            chapterContent = getChapterContent(url)
            if chapterContent == None:
                continue
            with open(dist, "a+", encoding="utf-8") as f:
                f.write(chapterContent)
        count += 1


def save2File(contents):
    distFolder = "./data/mianzhuan/"
    if not os.path.exists(distFolder):
        os.mkdir(distFolder)
    dist = distFolder + "index.txt"
    if os.path.exists(dist):
        os.remove(dist)
    with open(dist, "a+", encoding="utf-8") as f:
        for content in contents:
            f.write("{} \t {} \t \n".format(
                content["title"], content["url"]))


def main(baseUrl):
    contents = getContents(baseUrl)
    save2File(contents)
    savePerChapter2File(contents)
    print("FINISHED.")


if (__name__ == "__main__"):
    main(baseUrl)
