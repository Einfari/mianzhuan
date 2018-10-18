import requests

baseUrl = "https://www.baidu.com"

r = requests.get(baseUrl)

print(r.text)