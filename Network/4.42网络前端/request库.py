import requests

r = requests.get("https://www.baidu.com/")

print(r.status_code == requests.codes.ok)
