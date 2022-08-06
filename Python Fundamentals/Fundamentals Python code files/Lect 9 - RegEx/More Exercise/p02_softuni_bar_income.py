import re

valid_name_search = r"(?<=%)[A-Z][a-z]+(?=%)"
valid_product_search = r"(?<=<)\w+(?=>)"
valid_count_search = r"(?<=\|)\d+(?=\|)"
valid_price_search = r"\d+(.\d+)?(?=\$)"

total = 0
while True:
    entry = input()
    if entry == "end of shift":
        break
    try:
        name, product, count, price = [
            re.search(valid_name_search, entry).group(),
            re.search(valid_product_search, entry).group(),
            int(re.search(valid_count_search, entry).group()),
            float(re.search(valid_price_search, entry).group())
        ]
    except:
        continue
    current_total = count * price
    total += current_total
    print(f"{name}: {product} - {current_total:.2f}")
print(f"Total income: {total:.2f}")





