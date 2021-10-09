import json
a = [1,2,3]
b = 1
c = {"a","b"}
#以json的形式写入文件
with open("data.json","r") as f:
    content = json.load(f)

print(content)
print(type(content))