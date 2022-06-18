group_start = int(input())
days = int(input())
group = group_start
coins = 0
for day in range(1, days+1):

    if day % 10 == 0:   #10th day 2 leave
        group -= 2
    if day % 15 == 0:   #15th day 5 join
        group += 5
    coins += (50 - 2 * group)
    if day % 3 == 0:    #motivation
        coins -= 3 * group
    if day % 5 == 0:    #boss monster
        coins += 20 * group
        if day % 3 == 0:
            coins -= 2 * group
print(f"{group} companions received {(int(coins/group))} coins each.")

