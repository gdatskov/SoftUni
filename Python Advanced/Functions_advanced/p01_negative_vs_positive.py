def is_positive(x):
    if x > 0:
        return True
    else:
        return False


negatives = 0
positives = 0

numbers = [int(x) for x in input().split(" ")]

for x in numbers:
    if is_positive(x):
        positives += x
    else:
        negatives += x

print(negatives)
print(positives)

if abs(negatives) > positives:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
