#vacation = input
#puzzle=2.60
#doll=3.00
#bear=4.10
#minion=8.20
#truck=2.00
#if > 50 then discount 25% from total
#from total 10% for lease
#output "Yes! {left money} lv left.
#output "Not enough money! {money needed} lv needed.

vacation = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

toys = puzzles+dolls+bears+minions+trucks
price = puzzles*2.6+dolls*3+bears*4.1+minions*8.2+trucks*2
money = price*.9

if toys < 50:
    if money > vacation:
        print(f"Yes! {money-vacation:.2f} lv left.")
    else:
        print(f"Not enough money! {vacation-money:.2f} lv needed.")
else:
    money = money*.75
    if money > vacation:
        print(f"Yes! {money-vacation:.2f} lv left.")
    else:
        print(f"Not enough money! {vacation-money:.2f} lv needed.")
