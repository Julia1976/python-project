import requests

target = "https://shequ.codemao.cn/"
req = requests.get(url=target)
print(req.text)
