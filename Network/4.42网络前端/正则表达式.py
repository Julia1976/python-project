import re
codemao = "I love Codemao!"

pattern = re.compile(r"Code")
find_list = pattern.findall(codemao)

print(find_list)