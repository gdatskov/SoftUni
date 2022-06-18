city = input()
sales = float(input())

commission = -1

if 0 <= sales <= 500:
    if city == "Sofia":
        commission = 5
    elif city == "Varna":
        commission = 4.5
    elif city == "Plovdiv":
        commission = 5.5
if 500 < sales <= 1000:
    if city == "Sofia":
        commission = 7
    elif city == "Varna":
        commission = 7.5
    elif city == "Plovdiv":
        commission = 8
if 1000 < sales <= 10000:
    if city == "Sofia":
        commission = 8
    elif city == "Varna":
        commission = 10
    elif city == "Plovdiv":
        commission = 12
if sales > 10000:
    if city == "Sofia":
        commission = 12
    elif city == "Varna":
        commission = 13
    elif city == "Plovdiv":
        commission = 14.5

if commission < 0:
    print("error")
else:
    print(f"{sales*commission/100:.2f}")
