from math import ceil

show_name = input()
show_time = int(input())
free_time = int(input())

lunch_time = free_time/8
recreation_time = free_time/4
needed_time = lunch_time+recreation_time+show_time



if free_time>=needed_time:
    print(f"You have enough time to watch {show_name} and left "
          f"with {ceil(-needed_time+free_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {show_name}, "
          f"you need {ceil(needed_time-free_time)} more minutes.")