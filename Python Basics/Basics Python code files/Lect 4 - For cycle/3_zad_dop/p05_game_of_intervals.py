game_rounds = int(input())

result = 0
from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_49 = 0
invalid_numbers = 0

for rounds in range(game_rounds):
    input_number = int(input())
    if 0 <= input_number <= 9:
        result += input_number * 0.2
        from_0_to_9 += 1
    elif 10 <= input_number <= 19:
        result += input_number * 0.3
        from_10_to_19 += 1
    elif 20 <= input_number <= 29:
        result += input_number * 0.4
        from_20_to_29 += 1
    elif 30 <= input_number <= 39:
        result += 50
        from_30_to_39 += 1
    elif 40 <= input_number <= 50:
        result += 100
        from_40_to_49 += 1
    else:
        result = result / 2
        invalid_numbers += 1


print(f"{result:.2f}")
print(f"From 0 to 9: {from_0_to_9/game_rounds*100:.2f}%")
print(f"From 10 to 19: {from_10_to_19/game_rounds*100:.2f}%")
print(f"From 20 to 29: {from_20_to_29/game_rounds*100:.2f}%")
print(f"From 30 to 39: {from_30_to_39/game_rounds*100:.2f}%")
print(f"From 40 to 50: {from_40_to_49/game_rounds*100:.2f}%")
print(f"Invalid numbers: {invalid_numbers/game_rounds*100:.2f}%")
