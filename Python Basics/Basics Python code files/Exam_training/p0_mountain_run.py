from math import floor

record = float(input())
distance = float(input())
meters_per_second = float(input())

perfect_time = distance*meters_per_second
slow_time = floor(distance//50 * 30)
real_time = (perfect_time+slow_time)
if real_time < record:
    print(f" Yes! The new record is {real_time:.2f} seconds.")
else:
    print(f"No! He was {real_time-record:.2f} seconds slower.")
