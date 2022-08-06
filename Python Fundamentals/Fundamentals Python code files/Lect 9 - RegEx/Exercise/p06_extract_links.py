import re


search_pattern = r"www.([a-zA-Z0-9-])+(\.[a-z]+){1,}"

while True:
    text = input()
    if not text:
        break
    matches = re.finditer(search_pattern, text)
    for website in matches:
        print(website.group())
