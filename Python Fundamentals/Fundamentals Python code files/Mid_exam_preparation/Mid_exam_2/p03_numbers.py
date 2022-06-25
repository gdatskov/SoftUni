numbers = [int(x) for x in input().strip().split(" ")]

average = sum(numbers)/len(numbers)
numbers = [x for x in sorted(numbers, reverse=True) if x > average][:5]

if numbers:
    print(" ".join([str(x) for x in numbers]))
else:
    print("No")
