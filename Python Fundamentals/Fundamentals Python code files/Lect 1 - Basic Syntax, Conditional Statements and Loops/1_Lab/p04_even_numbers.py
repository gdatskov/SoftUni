count = int(input())
odd = False
remember = int
for i in range(count):
    number = int(input())
    if number % 2 != 0:
        odd = True
        remember = number
        break
if odd:
    print(f"{remember} is odd!")
else:
    print("All numbers are even.")