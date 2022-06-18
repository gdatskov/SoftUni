sport = ""
daily_win = 0
total_money = 0
days = int(input())
for day in range(1, days+1):
    count_result = 0
    day_money = 0
    while True:
        sport = input()
        if sport == "Finish":
             break
        result = input()
        if result == "win":
            count_result += 1
            day_money += 20
        else:
            count_result -= 1
    if count_result > 0:
        day_money = day_money * 1.1
        daily_win += 1
    else:
        daily_win -= 1
    total_money += day_money
if daily_win > 0:
    total_money = total_money * 1.2
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")



