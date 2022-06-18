entry = input()
li = entry.split(", ")
count = 0
while "0" in li:
    li.remove("0")
    count += 1
for i in range(count):
    li.append("0")
li = ", ".join(li)
print(f"[{li}]")