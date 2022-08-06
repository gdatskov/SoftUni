import re


text = input()
search_pattern = r"(^|(?<=\s))([a-zA-Z0-9]+[-._]?)+@+(\w+[-]?)+([.]+\w+){1,}"
res = re.finditer(search_pattern, text)

for i in res:
    print(i.group())