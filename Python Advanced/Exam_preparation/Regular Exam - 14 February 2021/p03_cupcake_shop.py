def stock_availability(lis, action, *args):
    if action == "delivery":
        lis.extend(args)
    else:
        if not args:
            lis.remove(lis[0])
        for param in args:
            if isinstance(param, int):
                number = param
                lis = lis[number:]
                break
            else:
                if param in lis:
                    while param in lis:
                        lis.remove(param)
    return lis




print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
