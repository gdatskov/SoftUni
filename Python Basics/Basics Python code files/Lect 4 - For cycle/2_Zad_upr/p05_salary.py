open_tabs = int(input())
salary = float(input())

for tabs in range(open_tabs):
    if salary > 0:
        tab = input()
        if tab == "Facebook":
            salary -= 150
        if tab == "Instagram":
            salary -= 100
        if tab == "Reddit":
            salary -= 50
    else:
        break
if salary > 0:
    print(int(salary))
else:
    print("You have lost your salary.")