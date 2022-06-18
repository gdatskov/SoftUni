import math

pages=int(input())
pages_per_hour=int(input())
days=int(input())
hours_per_day=pages/pages_per_hour/days
print(math.ceil(hours_per_day))


