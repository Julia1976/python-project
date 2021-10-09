import requests
import re

r = requests.get('https://codemao.cn/')
txt = r.text

#print(txt)

pattern = re.compile(r"https://[^\s]*png")
imglist = re.findall(pattern,txt)
print(imglist)

pattern = re.compile(r"https://[^\s]*jpg")
imglist_1 = re.findall(pattern,txt)
print(imglist_1)
