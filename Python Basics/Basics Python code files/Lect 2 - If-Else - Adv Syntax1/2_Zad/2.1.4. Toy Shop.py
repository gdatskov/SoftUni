vacation = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

toys = puzzles+dolls+bears+minions+trucks
price = puzzles*2.6+dolls*3+bears*4.1+minions*8.2+trucks*2
money = price*0.9

if toys < 50:
    money = money * 0.75

if money > vacation:
    print(f"Yes! {money-vacation:.2f} lv left.")
else:
    print(f"Not enough money! {vacation-money:.2f} lv needed.")
