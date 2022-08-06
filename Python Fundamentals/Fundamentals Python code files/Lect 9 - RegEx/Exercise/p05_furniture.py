import re

validation_pattern = r">>\w+<<\d+[.]?\d+!\d+"
extract_pattern = r"[a-zA-Z]+|[\d.?]+"

total = 0
bought_furniture = []


while True:
    text = input()
    if text == "Purchase":
        break
    match = re.search(validation_pattern, text)
    if match:
        result = re.findall(extract_pattern, text)
        bought_furniture.append(result[0])
        price, quantity = [float(x) for x in result[1:]]
        total += price * quantity

# if bought_furniture:
print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total:.2f}")