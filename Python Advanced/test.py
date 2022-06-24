test = ("asd", "fds", )
sale = True if any(x.isdigit() for x in test) else False
print(sale)

sale = True if any(x.isdigit() for x in (str(y) for y in args)) else False