def factorial(num):
    result = 1
    for i in range(num):
        result *= (i+1)
    return result


number1 = int(input())
number2 = int(input())

print(f"{factorial(number1)/factorial(number2):.2f}")
