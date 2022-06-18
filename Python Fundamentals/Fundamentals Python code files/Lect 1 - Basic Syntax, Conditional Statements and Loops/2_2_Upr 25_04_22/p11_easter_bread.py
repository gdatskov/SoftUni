budget = float(input())
flour = float(input())
pack_of_eggs = flour*0.75
milk = flour*1.25
loaf = pack_of_eggs + flour + milk/4
count = 0
colored_eggs = 0

while budget >= loaf:
    budget -= loaf
    count += 1
    colored_eggs += 3
    if count % 3 == 0:
        colored_eggs -= count-2

print(f"You made {count} loaves of Easter bread! "
      f"Now you have {int(colored_eggs)} eggs and {budget:.2f}BGN left.")
