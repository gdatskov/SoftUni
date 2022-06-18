record = float(input())  #seconds
distance = float(input())  #meters
speed_inverted = float(input())  #seconds per meter

speed = 1 / speed_inverted  #sorry, I work in SI!
resistances = distance // 15  #using decrements instead of coefficient = stupid
resistance_time = resistances * 12.5  #resistance conversion to stupid units...

time = distance / speed + resistance_time  #adding resistance instead of calculating resistance

if time < record:
    print(f"Yes, he succeeded! The new world record is {time:.2f} seconds.")
else:
    print(f"No, he failed! He was {time - record:.2f} seconds slower.")
