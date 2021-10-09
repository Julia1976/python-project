import urllib
import urllib.request

url = "https://shequ.codemao.cn/"
response = urllib.request.urlopen(url)
html = response.read()

print(html.decode("utf-8"))
