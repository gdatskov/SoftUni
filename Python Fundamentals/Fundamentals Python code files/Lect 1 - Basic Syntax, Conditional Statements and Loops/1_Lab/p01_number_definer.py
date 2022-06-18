# Write a program that reads a floating-point number and:
# -	prints "zero" if the number is zero
# -	prints "positive" or "negative"
# -	adds "small" if the absolute value of the number is less than 1 and it is not 0, or "large" if it exceeds
# 1 000 000

number = float(input())
if number == 0:
    print("zero")
else:
    if abs(number) < 1:
        print("small", end=" ")
    elif abs(number) > 1000000:
        print("large", end=" ")
    if number > 0:
        print("positive")
    else:
        print("negative")

