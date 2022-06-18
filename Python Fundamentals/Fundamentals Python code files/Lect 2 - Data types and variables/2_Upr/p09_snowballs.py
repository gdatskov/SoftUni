balls = int(input())
value = 0
best = 0
time = 1
weight = 0
quality = 0
for ball in range(balls):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value = int((weight / time) ** quality)
    if value > best:
        best = value
        best_list = [weight, time, value, quality]
print(f"{best_list[0]} : {best_list[1]} = {best_list[2]} ({best_list[3]})")
