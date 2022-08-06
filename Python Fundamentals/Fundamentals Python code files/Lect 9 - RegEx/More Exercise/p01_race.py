import re

participants = input().split(", ")
results = {}

while True:
    info = input()
    if info == "end of race":
        break
    name = "".join(re.findall(r"[a-zA-Z]", info))
    distance = sum(int(x) for x in re.findall(r"\d", info))
    if name in participants:
        if name not in results.keys():
            results[name] = distance
        else:
            results[name] += distance

sort = sorted(results.items(), key=lambda x: -x[1])
first, second, third = [x[0] for x in sort[:3]]
print(f"1st place: {first}")
print(f"2nd place: {second}")
print(f"3rd place: {third}")

