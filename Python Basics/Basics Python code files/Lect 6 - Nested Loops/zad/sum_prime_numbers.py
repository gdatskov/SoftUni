sum_prime = 0
sum_non_prime = 0


while True:
    entry = input()
    prime = True
    if entry == "stop":
        break
    entry = int(entry)
    if entry < 0:
        print("Number is negative.")
        entry = 0
    for i in range(2, entry):
        check = entry % i
        if entry % i == 0:
            prime = False
    if prime:
        sum_prime += entry
    else:
        sum_non_prime += entry
print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")




