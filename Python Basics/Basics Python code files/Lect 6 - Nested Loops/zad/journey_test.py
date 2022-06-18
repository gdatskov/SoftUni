destination = ""
current_budget = 0
budget_entry = 0.0

while destination != "End":
    destination = input()
    if destination == "End":
        break
    minimum_budget = float(input())
    while current_budget < minimum_budget:
        budget_entry = float(input())
        current_budget += budget_entry
        if current_budget >= minimum_budget:
            print(f"Going to {destination}!")
            current_budget = 0
            break
