import requests
from bs4 import BeautifulSoup

html_source = 'https://api.codemao.cn/web/banners/all?type=OFFICIAL'

html = requests.get(html_source)
data = html.json()
print(data["items"][0]["background_url"])
