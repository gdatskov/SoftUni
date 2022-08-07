import re


search_pattern = r"([=/])([A-Z]{1}[A-Za-z]{2,})\1"
string = input()

result = re.findall(search_pattern, string)
print(f"Destinations: {', '.join([res[1] for res in result])}")
print(f"Travel Points: {sum([len(res[1]) for res in result])}")
