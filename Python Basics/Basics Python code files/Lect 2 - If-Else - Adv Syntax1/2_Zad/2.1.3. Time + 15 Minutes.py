hour = int(input())
minute = int(input())

time = hour*60 + minute

time_fifteen = time + 15

if time_fifteen >= 24*60:
    time_fifteen = time_fifteen - 24*60

if (time_fifteen%60) > 9:
    print(f"{time_fifteen//60}:{(time_fifteen)%60}")
else: print(f"{time_fifteen//60}:0{(time_fifteen)%60}")
