number = int(input())
for i in range(number):
    check = input()
    if "," in check or "." in check or "_" in check:
        print(f"{check} is not pure!")
    else:
        print(f"{check} is pure.")
