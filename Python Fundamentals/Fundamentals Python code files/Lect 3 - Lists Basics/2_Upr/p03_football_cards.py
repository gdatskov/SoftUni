list_a=[]
list_b=[]

for a in range(11):
    list_a.append(f"A-{a+1}")
    list_b.append(f"B-{a+1}")

red_list_a = []
red_list_b = []

cards_list = input().split(" ")

for i in cards_list:
    if "A" in i:
        if i not in red_list_a:
            list_a.remove(i)
            red_list_a.append(i)
    if "B" in i:
        if i not in red_list_b:
            list_b.remove(i)
            red_list_b.append(i)
    if len(list_a) < 7 or len(list_b) < 7:
        break
print(f"Team A - {len(list_a)}; Team B - {len(list_b)}")
if len(list_a) < 7 or len(list_b) < 7:
    print("Game was terminated")
